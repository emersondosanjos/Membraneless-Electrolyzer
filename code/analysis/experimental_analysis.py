"""
Experimental data analysis for the membraneless electrolyzer.

This module provides functions to load, process, and analyze experimental
data from the membraneless electrolyzer tests.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
import os

class ExperimentalAnalysis:
    """
    Class for analyzing experimental data from membraneless electrolyzer tests.
    """
    
    def __init__(self, data_path="../data/experimental"):
        """
        Initialize the analysis with data path.
        
        Parameters:
        -----------
        data_path : str
            Path to experimental data directory
        """
        self.data_path = data_path
        self.iv_data = None
        self.h2_data = None
        
    def load_iv_data(self, filename="current_voltage_measurements.csv"):
        """
        Load current-voltage measurement data.
        
        Parameters:
        -----------
        filename : str
            Name of the IV data file
            
        Returns:
        --------
        pandas.DataFrame
            Loaded IV data
        """
        filepath = os.path.join(self.data_path, filename)
        self.iv_data = pd.read_csv(filepath, comment='#')
        return self.iv_data
    
    def load_h2_data(self, filename="hydrogen_production_rates.csv"):
        """
        Load hydrogen production rate data.
        
        Parameters:
        -----------
        filename : str
            Name of the H2 data file
            
        Returns:
        --------
        pandas.DataFrame
            Loaded H2 production data
        """
        filepath = os.path.join(self.data_path, filename)
        self.h2_data = pd.read_csv(filepath, comment='#')
        return self.h2_data
    
    def calculate_performance_metrics(self):
        """
        Calculate key performance metrics from experimental data.
        
        Returns:
        --------
        dict
            Dictionary containing performance metrics
        """
        if self.iv_data is None:
            self.load_iv_data()
        if self.h2_data is None:
            self.load_h2_data()
        
        metrics = {}
        
        # Current density at different voltages
        metrics['current_at_1_5V'] = self.interpolate_current(1.5)
        metrics['current_at_2_0V'] = self.interpolate_current(2.0)
        
        # Maximum current density
        metrics['max_current_density'] = self.iv_data['current_density_A_m2'].max()
        
        # Voltage at specific current densities
        metrics['voltage_at_100_A_m2'] = self.interpolate_voltage(100)
        metrics['voltage_at_200_A_m2'] = self.interpolate_voltage(200)
        
        # Average Faradaic efficiency
        metrics['avg_faradaic_efficiency'] = self.h2_data['faradaic_efficiency'].mean()
        metrics['min_faradaic_efficiency'] = self.h2_data['faradaic_efficiency'].min()
        
        # Maximum hydrogen production rate
        metrics['max_h2_rate_mmol_s'] = self.h2_data['h2_production_mmol_s'].max()
        
        return metrics
    
    def interpolate_current(self, voltage):
        """
        Interpolate current density at a given voltage.
        
        Parameters:
        -----------
        voltage : float
            Voltage in V
            
        Returns:
        --------
        float
            Interpolated current density in A/m²
        """
        if self.iv_data is None:
            self.load_iv_data()
        
        return np.interp(voltage, 
                        self.iv_data['voltage_V'], 
                        self.iv_data['current_density_A_m2'])
    
    def interpolate_voltage(self, current_density):
        """
        Interpolate voltage at a given current density.
        
        Parameters:
        -----------
        current_density : float
            Current density in A/m²
            
        Returns:
        --------
        float
            Interpolated voltage in V
        """
        if self.iv_data is None:
            self.load_iv_data()
        
        return np.interp(current_density,
                        self.iv_data['current_density_A_m2'],
                        self.iv_data['voltage_V'])
    
    def fit_tafel_equation(self, voltage_range=(1.2, 1.8)):
        """
        Fit Tafel equation to the experimental data.
        
        Parameters:
        -----------
        voltage_range : tuple
            Voltage range for fitting (V)
            
        Returns:
        --------
        dict
            Fitting parameters and statistics
        """
        if self.iv_data is None:
            self.load_iv_data()
        
        # Filter data in the specified voltage range
        mask = ((self.iv_data['voltage_V'] >= voltage_range[0]) & 
                (self.iv_data['voltage_V'] <= voltage_range[1]))
        
        voltage = self.iv_data.loc[mask, 'voltage_V'].values
        current = self.iv_data.loc[mask, 'current_density_A_m2'].values
        
        # Tafel equation: eta = a + b * log(i)
        # Rearranged: i = exp((eta - a) / b)
        def tafel_equation(eta, a, b):
            return np.exp((eta - a) / b)
        
        # Fit the equation
        popt, pcov = curve_fit(tafel_equation, voltage, current, 
                              p0=[1.0, 0.1], maxfev=5000)
        
        # Calculate R²
        y_pred = tafel_equation(voltage, *popt)
        ss_res = np.sum((current - y_pred) ** 2)
        ss_tot = np.sum((current - np.mean(current)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)
        
        return {
            'a': popt[0],          # Tafel constant (V)
            'b': popt[1],          # Tafel slope (V/decade)
            'r_squared': r_squared,
            'covariance': pcov,
            'voltage_range': voltage_range
        }
    
    def plot_iv_curve(self, save_path=None, show_fit=True):
        """
        Plot the current-voltage characteristic curve.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        show_fit : bool
            Whether to show Tafel fit
        """
        if self.iv_data is None:
            self.load_iv_data()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Linear plot
        ax1.errorbar(self.iv_data['voltage_V'], 
                    self.iv_data['current_density_A_m2'],
                    yerr=self.iv_data['uncertainty_A'] * 10000,  # Convert to A/m²
                    fmt='o-', capsize=3, label='Experimental')
        
        ax1.set_xlabel('Voltage (V)')
        ax1.set_ylabel('Current Density (A/m²)')
        ax1.set_title('Current-Voltage Characteristic')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Semi-log plot
        ax2.semilogy(self.iv_data['voltage_V'], 
                    self.iv_data['current_density_A_m2'],
                    'o-', label='Experimental')
        
        if show_fit:
            tafel_fit = self.fit_tafel_equation()
            voltage_fit = np.linspace(1.2, 1.8, 100)
            current_fit = np.exp((voltage_fit - tafel_fit['a']) / tafel_fit['b'])
            ax2.semilogy(voltage_fit, current_fit, 'r--', 
                        label=f'Tafel fit (R² = {tafel_fit["r_squared"]:.3f})')
        
        ax2.set_xlabel('Voltage (V)')
        ax2.set_ylabel('Current Density (A/m²)')
        ax2.set_title('Current-Voltage (Semi-log)')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def plot_h2_production(self, save_path=None):
        """
        Plot hydrogen production rate analysis.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        """
        if self.h2_data is None:
            self.load_h2_data()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Production rate vs current density
        ax1.plot(self.h2_data['current_density_A_m2'], 
                self.h2_data['h2_production_mmol_s'],
                'o-', label='Experimental')
        
        # Theoretical line (100% Faradaic efficiency)
        theoretical = self.h2_data['current_density_A_m2'] * 0.01 / (2 * 96485) * 1000
        ax1.plot(self.h2_data['current_density_A_m2'], 
                theoretical, 'r--', label='Theoretical (100% efficiency)')
        
        ax1.set_xlabel('Current Density (A/m²)')
        ax1.set_ylabel('H₂ Production Rate (mmol/s)')
        ax1.set_title('Hydrogen Production Rate')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Faradaic efficiency
        ax2.errorbar(self.h2_data['current_density_A_m2'],
                    self.h2_data['faradaic_efficiency'],
                    yerr=self.h2_data['uncertainty_efficiency'],
                    fmt='o-', capsize=3)
        
        ax2.axhline(y=1.0, color='r', linestyle='--', alpha=0.7, label='Perfect efficiency')
        ax2.set_xlabel('Current Density (A/m²)')
        ax2.set_ylabel('Faradaic Efficiency')
        ax2.set_title('Faradaic Efficiency')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        ax2.set_ylim(0.98, 1.03)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generate_summary_report(self):
        """
        Generate a summary report of the experimental analysis.
        
        Returns:
        --------
        str
            Formatted summary report
        """
        metrics = self.calculate_performance_metrics()
        tafel_fit = self.fit_tafel_equation()
        
        report = f"""
EXPERIMENTAL ANALYSIS SUMMARY
============================

Current-Voltage Performance:
---------------------------
• Current density at 1.5 V: {metrics['current_at_1_5V']:.1f} A/m²
• Current density at 2.0 V: {metrics['current_at_2_0V']:.1f} A/m²
• Maximum current density: {metrics['max_current_density']:.1f} A/m²
• Voltage at 100 A/m²: {metrics['voltage_at_100_A_m2']:.2f} V
• Voltage at 200 A/m²: {metrics['voltage_at_200_A_m2']:.2f} V

Hydrogen Production:
-------------------
• Maximum H₂ rate: {metrics['max_h2_rate_mmol_s']:.3f} mmol/s
• Average Faradaic efficiency: {metrics['avg_faradaic_efficiency']:.3f}
• Minimum Faradaic efficiency: {metrics['min_faradaic_efficiency']:.3f}

Tafel Analysis:
--------------
• Tafel slope: {tafel_fit['b']*1000:.1f} mV/decade
• Tafel constant: {tafel_fit['a']:.3f} V
• Fit quality (R²): {tafel_fit['r_squared']:.3f}

Data Quality:
------------
• Number of IV data points: {len(self.iv_data) if self.iv_data is not None else 0}
• Number of H₂ data points: {len(self.h2_data) if self.h2_data is not None else 0}
• Voltage range: {self.iv_data['voltage_V'].min():.1f} - {self.iv_data['voltage_V'].max():.1f} V
        """
        
        return report

if __name__ == "__main__":
    # Example usage
    analysis = ExperimentalAnalysis()
    
    # Load and analyze data
    iv_data = analysis.load_iv_data()
    h2_data = analysis.load_h2_data()
    
    # Generate plots
    analysis.plot_iv_curve()
    analysis.plot_h2_production()
    
    # Print summary
    print(analysis.generate_summary_report())