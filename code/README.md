# Code Directory

This directory contains all computational scripts and models used in the theoretical and experimental analysis of the membraneless electrolyzer.

## Structure

```
code/
├── simulations/        # Theoretical models and simulations
├── analysis/          # Data analysis scripts
├── plotting/          # Visualization scripts
└── utils/             # Utility functions and helpers
```

## File Descriptions

### Simulations
- **`electrolyzer_model.py`**: Main theoretical model for the membraneless electrolyzer
- **`mass_transport.py`**: Mass transport calculations and analysis
- **`electrochemical_kinetics.py`**: Electrochemical reaction kinetics modeling

### Analysis
- **`experimental_analysis.py`**: Processing and analysis of experimental data
- **`performance_metrics.py`**: Calculation of electrolyzer performance parameters
- **`parameter_estimation.py`**: Parameter fitting and optimization routines

### Plotting
- **`figure_generation.py`**: Scripts to generate figures for the manuscript
- **`supplementary_plots.py`**: Additional visualization scripts

### Utils
- **`constants.py`**: Physical constants and system parameters
- **`helper_functions.py`**: Common utility functions

## Usage

Each script includes detailed documentation and examples. To run the main analysis:

```python
# Example usage
from simulations.electrolyzer_model import MembranelessElectrolyzer
from analysis.experimental_analysis import process_data

# Load and analyze data
model = MembranelessElectrolyzer()
results = model.simulate()
```

## Dependencies

See `../requirements.txt` for required Python packages.