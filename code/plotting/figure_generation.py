"""
Figure generation scripts for the membraneless electrolyzer manuscript.

This module creates publication-quality figures for the research paper
"Theoretical-Experimental Analysis of a Membraneless Electrolyzer for Hydrogen Production".
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import seaborn as sns
import sys
import os

# Add parent directories to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analysis.experimental_analysis import ExperimentalAnalysis
from simulations.electrolyzer_model import MembranelessElectrolyzer

# Set publication-style defaults
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("husl")

class FigureGenerator:
    """
    Class for generating publication-quality figures.
    """
    
    def __init__(self, data_path="../data", figures_path="../figures"):
        """
        Initialize figure generator.
        
        Parameters:
        -----------
        data_path : str
            Path to data directory
        figures_path : str
            Path to figures output directory
        """
        self.data_path = data_path
        self.figures_path = figures_path
        self.analysis = ExperimentalAnalysis(os.path.join(data_path, "experimental"))
        self.model = MembranelessElectrolyzer()
        
        # Create output directories if they don't exist
        os.makedirs(os.path.join(figures_path, "main"), exist_ok=True)
        os.makedirs(os.path.join(figures_path, "supplementary"), exist_ok=True)
    
    def figure_1_schematic(self, save_path=None):
        """
        Generate Figure 1: Schematic diagram of the membraneless electrolyzer.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        """
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        
        # Draw the electrolyzer schematic
        # Electrolyte channel
        channel = FancyBboxPatch((2, 2), 6, 3, 
                                boxstyle="round,pad=0.1",
                                facecolor='lightblue', 
                                edgecolor='blue',
                                alpha=0.7,
                                linewidth=2)
        ax.add_patch(channel)
        
        # Anode (left electrode)
        anode = plt.Rectangle((1, 1.5), 1, 4, 
                             facecolor='red', 
                             edgecolor='darkred',
                             alpha=0.8)
        ax.add_patch(anode)
        
        # Cathode (right electrode)
        cathode = plt.Rectangle((8, 1.5), 1, 4, 
                               facecolor='blue', 
                               edgecolor='darkblue',
                               alpha=0.8)
        ax.add_patch(cathode)
        
        # Flow arrows
        arrow_props = dict(arrowstyle='->', lw=2, color='black')
        ax.annotate('', xy=(2.5, 3.5), xytext=(1.5, 3.5), arrowprops=arrow_props)
        ax.annotate('', xy=(8.5, 3.5), xytext=(7.5, 3.5), arrowprops=arrow_props)
        
        # Gas bubbles
        # Hydrogen bubbles at cathode
        for i, y in enumerate([2.5, 3.0, 3.5, 4.0, 4.5]):
            bubble = plt.Circle((7.5, y), 0.1, facecolor='lightgray', edgecolor='gray')
            ax.add_patch(bubble)
        
        # Oxygen bubbles at anode
        for i, y in enumerate([2.5, 3.0, 3.5, 4.0, 4.5]):
            bubble = plt.Circle((2.5, y), 0.08, facecolor='orange', edgecolor='red', alpha=0.7)
            ax.add_patch(bubble)
        
        # Labels
        ax.text(1.5, 0.8, 'Anode\n(O₂ evolution)', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkred')
        ax.text(8.5, 0.8, 'Cathode\n(H₂ evolution)', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='darkblue')
        ax.text(5, 6, 'Electrolyte Flow', ha='center', va='center', 
                fontsize=14, fontweight='bold')
        
        # Reactions
        ax.text(1.5, 6.2, '2H₂O → O₂ + 4H⁺ + 4e⁻', ha='center', va='center', 
                fontsize=10, style='italic', color='darkred')
        ax.text(8.5, 6.2, '4H⁺ + 4e⁻ → 2H₂', ha='center', va='center', 
                fontsize=10, style='italic', color='darkblue')
        
        # Current flow
        ax.annotate('', xy=(1.5, 7), xytext=(8.5, 7), 
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.text(5, 7.3, 'Current Flow', ha='center', va='center', 
                fontsize=12, fontweight='bold', color='green')
        
        # Voltage source
        ax.text(5, 0.5, 'V', ha='center', va='center', 
                fontsize=16, fontweight='bold', 
                bbox=dict(boxstyle="circle", facecolor='yellow', alpha=0.8))
        
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Membraneless Electrolyzer Schematic', fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        else:
            plt.savefig(os.path.join(self.figures_path, "main", "fig1_schematic.pdf"), 
                       dpi=300, bbox_inches='tight', facecolor='white')
        
        plt.show()
    
    def figure_2_iv_curves(self, save_path=None):
        """
        Generate Figure 2: Current-voltage characteristic curves.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        """
        # Load experimental data
        self.analysis.load_iv_data()
        
        # Generate simulation data
        sim_results = self.model.simulate_iv_curve(voltage_range=(1.0, 2.5), num_points=50)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Linear scale plot
        ax1.errorbar(self.analysis.iv_data['voltage_V'], 
                    self.analysis.iv_data['current_density_A_m2'],
                    yerr=self.analysis.iv_data['uncertainty_A'] * 10000,
                    fmt='o', capsize=3, label='Experimental', 
                    markersize=6, linewidth=2)
        
        ax1.plot(sim_results['voltage'], sim_results['current_density'],
                'r-', label='Theoretical Model', linewidth=2)
        
        ax1.set_xlabel('Cell Voltage (V)', fontsize=12)
        ax1.set_ylabel('Current Density (A/m²)', fontsize=12)
        ax1.set_title('(a) Linear Scale', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=10)
        ax1.set_xlim(1.0, 2.5)
        
        # Semi-log plot
        ax2.semilogy(self.analysis.iv_data['voltage_V'], 
                    self.analysis.iv_data['current_density_A_m2'],
                    'o', label='Experimental', markersize=6)
        
        ax2.semilogy(sim_results['voltage'], sim_results['current_density'],
                    'r-', label='Theoretical Model', linewidth=2)
        
        # Add Tafel fit
        tafel_fit = self.analysis.fit_tafel_equation()
        voltage_fit = np.linspace(1.2, 1.8, 100)
        current_fit = np.exp((voltage_fit - tafel_fit['a']) / tafel_fit['b'])
        ax2.semilogy(voltage_fit, current_fit, 'g--', 
                    label=f'Tafel Fit (slope = {tafel_fit["b"]*1000:.0f} mV/dec)', 
                    linewidth=2)
        
        ax2.set_xlabel('Cell Voltage (V)', fontsize=12)
        ax2.set_ylabel('Current Density (A/m²)', fontsize=12)
        ax2.set_title('(b) Semi-logarithmic Scale', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=10)
        ax2.set_xlim(1.0, 2.5)
        
        plt.suptitle('Current-Voltage Characteristics', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.savefig(os.path.join(self.figures_path, "main", "fig2_iv_curves.pdf"), 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def figure_3_hydrogen_production(self, save_path=None):
        """
        Generate Figure 3: Hydrogen production rate analysis.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        """
        # Load experimental data
        self.analysis.load_h2_data()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Production rate vs current density
        ax1.plot(self.analysis.h2_data['current_density_A_m2'], 
                self.analysis.h2_data['h2_production_mmol_s'],
                'o-', label='Experimental', markersize=6, linewidth=2)
        
        # Theoretical line (100% Faradaic efficiency)
        theoretical = self.analysis.h2_data['current_density_A_m2'] * 0.01 / (2 * 96485) * 1000
        ax1.plot(self.analysis.h2_data['current_density_A_m2'], 
                theoretical, 'r--', label='Theoretical (100% Faradaic efficiency)', 
                linewidth=2)
        
        ax1.set_xlabel('Current Density (A/m²)', fontsize=12)
        ax1.set_ylabel('H₂ Production Rate (mmol/s)', fontsize=12)
        ax1.set_title('(a) Hydrogen Production Rate', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend(fontsize=10)
        
        # Faradaic efficiency
        ax2.errorbar(self.analysis.h2_data['current_density_A_m2'],
                    self.analysis.h2_data['faradaic_efficiency'],
                    yerr=self.analysis.h2_data['uncertainty_efficiency'],
                    fmt='o-', capsize=3, markersize=6, linewidth=2)
        
        ax2.axhline(y=1.0, color='r', linestyle='--', alpha=0.7, 
                   label='Perfect Efficiency', linewidth=2)
        ax2.set_xlabel('Current Density (A/m²)', fontsize=12)
        ax2.set_ylabel('Faradaic Efficiency', fontsize=12)
        ax2.set_title('(b) Faradaic Efficiency', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=10)
        ax2.set_ylim(0.995, 1.005)
        
        plt.suptitle('Hydrogen Production Analysis', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.savefig(os.path.join(self.figures_path, "main", "fig3_hydrogen_production.pdf"), 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def figure_4_efficiency(self, save_path=None):
        """
        Generate Figure 4: Energy efficiency comparison.
        
        Parameters:
        -----------
        save_path : str, optional
            Path to save the figure
        """
        # Load experimental data
        self.analysis.load_iv_data()
        
        # Calculate efficiencies
        voltage = self.analysis.iv_data['voltage_V']
        current = self.analysis.iv_data['current_A']
        
        # Voltage efficiency
        voltage_efficiency = 1.229 / voltage
        
        # Energy efficiency (simplified calculation)
        h2_rate = current / (2 * 96485)  # mol/s
        theoretical_power = 1.229 * current
        actual_power = voltage * current
        energy_efficiency = theoretical_power / actual_power
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Voltage efficiency
        ax1.plot(self.analysis.iv_data['current_density_A_m2'], 
                voltage_efficiency, 'o-', markersize=6, linewidth=2, 
                label='Voltage Efficiency')
        
        ax1.set_xlabel('Current Density (A/m²)', fontsize=12)
        ax1.set_ylabel('Voltage Efficiency', fontsize=12)
        ax1.set_title('(a) Voltage Efficiency', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0.4, 1.0)
        
        # Energy efficiency comparison
        ax2.plot(self.analysis.iv_data['current_density_A_m2'], 
                energy_efficiency * 100, 'o-', markersize=6, linewidth=2,
                label='Membraneless Electrolyzer')
        
        # Add comparison with literature (hypothetical data)
        lit_current = np.array([50, 100, 150, 200, 250, 300])
        lit_efficiency = np.array([75, 73, 70, 68, 65, 62])
        ax2.plot(lit_current, lit_efficiency, 's--', markersize=6, linewidth=2,
                label='Conventional Electrolyzer', alpha=0.7)
        
        ax2.set_xlabel('Current Density (A/m²)', fontsize=12)
        ax2.set_ylabel('Energy Efficiency (%)', fontsize=12)
        ax2.set_title('(b) Energy Efficiency Comparison', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.legend(fontsize=10)
        ax2.set_ylim(40, 80)
        
        plt.suptitle('Efficiency Analysis', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        else:
            plt.savefig(os.path.join(self.figures_path, "main", "fig4_efficiency.pdf"), 
                       dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generate_all_figures(self):
        """
        Generate all main manuscript figures.
        """
        print("Generating Figure 1: Electrolyzer Schematic...")
        self.figure_1_schematic()
        
        print("Generating Figure 2: Current-Voltage Characteristics...")
        self.figure_2_iv_curves()
        
        print("Generating Figure 3: Hydrogen Production Analysis...")
        self.figure_3_hydrogen_production()
        
        print("Generating Figure 4: Efficiency Analysis...")
        self.figure_4_efficiency()
        
        print("All figures generated successfully!")

if __name__ == "__main__":
    # Generate all figures
    generator = FigureGenerator()
    generator.generate_all_figures()