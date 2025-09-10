# Reproducibility Guide

This document provides step-by-step instructions for reproducing all results presented in the manuscript "Theoretical-Experimental Analysis of a Membraneless Electrolyzer for Hydrogen Production".

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- Required Python packages (see `../requirements.txt`)
- MATLAB R2020a or higher (optional, for MATLAB verification scripts)
- Git for version control

### Hardware Requirements
- Minimum 8 GB RAM for simulation scripts
- Multi-core processor recommended for parametric studies
- Approximately 2 GB disk space for data and results

## Setup Instructions

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/emersondosanjos/Membraneless-Electrolyzer.git
cd Membraneless-Electrolyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Verification
```bash
# Verify data integrity (checksums will be provided)
python code/utils/verify_data.py
```

## Reproducing Results

### Figure 1: Electrolyzer Schematic
This figure is conceptual and created using external drawing software. The source files are available in `figures/raw/`.

### Figure 2: Current-Voltage Characteristics
```bash
# Process experimental data
python code/analysis/experimental_analysis.py --data data/experimental/current_voltage_measurements.csv

# Run theoretical model
python code/simulations/electrolyzer_model.py --output results/iv_simulation.csv

# Generate figure
python code/plotting/figure_generation.py --figure 2
```

### Figure 3: Hydrogen Production Rates
```bash
# Analyze production rate data
python code/analysis/performance_metrics.py --input data/experimental/hydrogen_production_rates.csv

# Generate figure
python code/plotting/figure_generation.py --figure 3
```

### Figure 4: Energy Efficiency Analysis
```bash
# Calculate efficiency metrics
python code/analysis/performance_metrics.py --efficiency --input data/experimental/efficiency_data.csv

# Generate figure
python code/plotting/figure_generation.py --figure 4
```

### Figure 5: Parametric Study
```bash
# Run parametric analysis
python code/simulations/parametric_study.py --parameters data/parameters/system_parameters.json

# Generate figure
python code/plotting/figure_generation.py --figure 5
```

## Validation Steps

### 1. Compare with Reference Data
```bash
# Run validation against reference results
python code/utils/validate_results.py
```

### 2. Statistical Analysis
```bash
# Perform statistical analysis
python code/analysis/statistical_analysis.py
```

### 3. Uncertainty Propagation
```bash
# Calculate uncertainties
python code/analysis/uncertainty_analysis.py
```

## Expected Outputs

After running all scripts, you should find:
- Generated figures in `figures/main/`
- Processed data in `data/processed/`
- Simulation results in `results/`
- Validation reports in `validation/`

## Troubleshooting

### Common Issues
1. **Memory errors**: Reduce simulation resolution in parameter files
2. **Package conflicts**: Use the exact versions specified in `requirements.txt`
3. **Data file errors**: Verify data integrity using checksums

### Getting Help
- Check the FAQ in each script's documentation
- Open an issue on GitHub for technical problems
- Contact authors for methodological questions

## Computational Time

Expected runtime on a standard desktop computer:
- Data processing: ~5 minutes
- Simulations: ~30 minutes
- Figure generation: ~10 minutes
- Total: ~45 minutes

## Citation

If you use these reproduction scripts, please cite both the original paper and this supplementary material.