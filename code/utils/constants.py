"""
Physical constants and system parameters for the membraneless electrolyzer model.

This module defines all constants, default parameters, and material properties
used throughout the simulation and analysis scripts.
"""

import numpy as np

# Physical constants
FARADAY_CONSTANT = 96485.3329  # C/mol
GAS_CONSTANT = 8.3144598      # J/mol/K
AVOGADRO_NUMBER = 6.02214076e23  # 1/mol

# Standard conditions
STANDARD_TEMPERATURE = 298.15  # K (25°C)
STANDARD_PRESSURE = 101325     # Pa (1 atm)

# Electrochemical constants
STANDARD_HYDROGEN_POTENTIAL = 0.0      # V vs SHE
STANDARD_OXYGEN_POTENTIAL = 1.229      # V vs SHE
THEORETICAL_CELL_VOLTAGE = 1.229       # V

# Water properties at 25°C
WATER_DENSITY = 997.0          # kg/m³
WATER_VISCOSITY = 8.9e-4       # Pa·s
WATER_MOLECULAR_WEIGHT = 18.015 # g/mol

# Ionic diffusion coefficients in water at 25°C (m²/s)
DIFFUSION_COEFFICIENTS = {
    'H+': 9.31e-9,
    'OH-': 5.27e-9,
    'H2': 4.5e-9,
    'O2': 2.0e-9,
    'H2O': 2.3e-9
}

# Electrode parameters (default values)
class ElectrodeParameters:
    """Default electrode parameters for the membraneless electrolyzer."""
    
    # Geometry
    LENGTH = 0.05              # m (5 cm)
    WIDTH = 0.02               # m (2 cm)
    THICKNESS = 0.001          # m (1 mm)
    ELECTRODE_SEPARATION = 0.005  # m (5 mm)
    
    # Kinetic parameters
    ANODE_EXCHANGE_CURRENT = 1e-3   # A/m²
    CATHODE_EXCHANGE_CURRENT = 1e-2  # A/m²
    ANODE_CHARGE_TRANSFER = 0.5     # dimensionless
    CATHODE_CHARGE_TRANSFER = 0.5   # dimensionless
    
    # Surface area enhancement
    ROUGHNESS_FACTOR = 100     # dimensionless

# Operating conditions (default values)
class OperatingConditions:
    """Default operating conditions for the membraneless electrolyzer."""
    
    TEMPERATURE = 298.15       # K (25°C)
    PRESSURE = 101325          # Pa (1 atm)
    INLET_VELOCITY = 0.01      # m/s
    ELECTROLYTE_CONCENTRATION = 1000  # mol/m³ (1 M)
    PH = 7.0                   # neutral pH

# Material properties
class MaterialProperties:
    """Material properties for electrodes and electrolyte."""
    
    # Electrode conductivity
    ELECTRODE_CONDUCTIVITY = 1e6    # S/m (typical for carbon electrodes)
    
    # Electrolyte conductivity (1 M NaCl)
    ELECTROLYTE_CONDUCTIVITY = 10.9  # S/m
    
    # Gas solubilities (mol/m³/Pa)
    HYDROGEN_SOLUBILITY = 7.8e-6
    OXYGEN_SOLUBILITY = 1.3e-5

# Numerical parameters
class NumericalParameters:
    """Parameters for numerical simulation."""
    
    # Mesh resolution
    MESH_ELEMENTS_X = 100
    MESH_ELEMENTS_Y = 50
    MESH_ELEMENTS_Z = 20
    
    # Convergence criteria
    RELATIVE_TOLERANCE = 1e-6
    ABSOLUTE_TOLERANCE = 1e-9
    MAX_ITERATIONS = 100
    
    # Time stepping (for transient simulations)
    TIME_STEP = 0.01           # s
    FINAL_TIME = 10.0          # s

def get_diffusion_coefficient(species, temperature=STANDARD_TEMPERATURE):
    """
    Get diffusion coefficient for a species at given temperature.
    
    Parameters:
    -----------
    species : str
        Chemical species name
    temperature : float
        Temperature in K
        
    Returns:
    --------
    float
        Diffusion coefficient in m²/s
    """
    base_coeff = DIFFUSION_COEFFICIENTS.get(species, 1e-9)
    
    # Temperature correction (approximate)
    temp_factor = (temperature / STANDARD_TEMPERATURE) * (WATER_VISCOSITY / get_water_viscosity(temperature))
    
    return base_coeff * temp_factor

def get_water_viscosity(temperature):
    """
    Calculate water viscosity as a function of temperature.
    
    Parameters:
    -----------
    temperature : float
        Temperature in K
        
    Returns:
    --------
    float
        Dynamic viscosity in Pa·s
    """
    # Vogel equation for water viscosity
    A = 0.02939
    B = 507.88
    C = 149.3
    
    T_celsius = temperature - 273.15
    viscosity = A * np.exp(B / (T_celsius + C))
    
    return viscosity * 1e-3  # Convert from cP to Pa·s

if __name__ == "__main__":
    # Print summary of constants
    print("Membraneless Electrolyzer Constants")
    print("=" * 40)
    print(f"Faraday constant: {FARADAY_CONSTANT:.1f} C/mol")
    print(f"Theoretical cell voltage: {THEORETICAL_CELL_VOLTAGE:.3f} V")
    print(f"Water density: {WATER_DENSITY:.1f} kg/m³")
    print(f"Water viscosity: {WATER_VISCOSITY*1000:.2f} cP")
    print("\nDiffusion coefficients at 25°C:")
    for species, coeff in DIFFUSION_COEFFICIENTS.items():
        print(f"  {species}: {coeff*1e9:.2f} × 10⁻⁹ m²/s")