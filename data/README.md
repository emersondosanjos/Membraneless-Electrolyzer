# Data Directory

This directory contains all experimental and simulation datasets referenced in the manuscript.

## Structure

```
data/
├── experimental/       # Experimental measurements
├── simulations/       # Simulation results
├── processed/         # Processed and cleaned datasets
└── parameters/        # System parameters and constants
```

## Data Files

### Experimental Data
- **`current_voltage_measurements.csv`**: I-V characteristic curves
- **`hydrogen_production_rates.csv`**: Measured H₂ production rates
- **`temperature_profiles.csv`**: Temperature measurements during operation
- **`efficiency_data.csv`**: Energy efficiency measurements

### Simulation Results
- **`theoretical_iv_curves.csv`**: Simulated current-voltage relationships
- **`mass_transport_profiles.csv`**: Concentration and velocity profiles
- **`parametric_studies.csv`**: Results from parameter sensitivity analysis

### Processed Data
- **`normalized_performance.csv`**: Normalized performance metrics
- **`statistical_analysis.csv`**: Statistical summaries and uncertainty analysis

### Parameters
- **`system_parameters.json`**: Electrolyzer geometry and operating conditions
- **`material_properties.json`**: Physical and chemical properties of materials
- **`experimental_conditions.json`**: Details of experimental setup and protocols

## Data Format

All CSV files use comma separation with headers. JSON files contain structured parameter sets with units and descriptions.

## Usage Notes

- All experimental data includes uncertainty estimates where applicable
- Simulation data is provided at the resolution used for publication figures
- Raw data is available upon request for replication studies

## Data Availability

This data supports the findings presented in "Theoretical-Experimental Analysis of a Membraneless Electrolyzer for Hydrogen Production" and is made available under the terms specified in the LICENSE file.