# Sample Data: Experimental Conditions

This file contains detailed information about the experimental conditions used to generate the data in this supplementary material.

## Equipment and Setup

### Electrolyzer Configuration
- **Cell type**: Membraneless flow-through design
- **Electrode material**: Carbon felt (Sigracell GFD 4.6 EA)
- **Electrode dimensions**: 50 mm × 20 mm × 1 mm (L × W × T)
- **Active area**: 10 cm² (per electrode)
- **Electrode separation**: 5 mm
- **Channel dimensions**: 50 mm × 20 mm × 5 mm (L × W × H)

### Electrolyte System
- **Electrolyte**: 1 M NaCl in deionized water
- **pH**: 7.0 ± 0.1 (buffered with phosphate)
- **Conductivity**: 10.9 ± 0.2 S/m (measured at 25°C)
- **Flow rate**: 10 mL/min (Reynolds number ≈ 50)
- **Temperature**: 25.0 ± 0.5°C

### Measurement Equipment
- **Power supply**: Keysight E36313A (0-6V, 0-3A)
- **Multimeter**: Keysight 34465A (6.5 digit)
- **Gas chromatograph**: Agilent 7890B with TCD detector
- **Flow meter**: Bronkhorst EL-FLOW Select (1-20 mL/min)
- **Temperature controller**: Julabo F25-ED circulator
- **pH meter**: Metrohm 827 pH lab

## Experimental Protocol

### Electrode Preparation
1. Carbon felt electrodes pre-treated in 1 M HCl for 24 hours
2. Rinsed with deionized water until pH neutral
3. Dried in oven at 80°C for 12 hours
4. Stored in desiccator until use

### System Setup
1. Electrolyzer assembled with fresh electrodes
2. System flushed with electrolyte for 30 minutes
3. Temperature stabilized at 25°C
4. Baseline measurements recorded

### Current-Voltage Measurements
1. **Voltage sweep**: 1.0 to 2.5 V in 0.1 V increments
2. **Hold time**: 2 minutes per voltage point
3. **Measurements**: Current recorded every 10 seconds
4. **Average**: Final 30 seconds used for data point
5. **Repeats**: 3 independent measurements per condition

### Hydrogen Production Analysis
1. **Gas collection**: 300 seconds per measurement point
2. **Sample volume**: 1 mL injected into GC
3. **Analysis**: H₂ concentration by thermal conductivity
4. **Calibration**: Daily calibration with certified gas standards
5. **Background**: Blank measurements with no current

### Quality Control
- System leak check before each experiment
- Electrolyte replaced every 4 hours of operation
- Electrode surface cleaned between experiments
- Temperature drift monitored (±0.1°C tolerance)
- Flow rate verified with independent flowmeter

## Data Processing

### Current-Voltage Data
- Raw current data averaged over final 30 seconds
- iR drop correction applied using measured resistance
- Uncertainty calculated from standard deviation of 3 repeats
- Current density calculated using geometric electrode area

### Hydrogen Production Data
- GC peak area converted to molar concentration
- Production rate calculated from flow rate and concentration
- Faradaic efficiency = (measured H₂) / (theoretical H₂)
- Background subtraction applied to all measurements

### Statistical Analysis
- Error bars represent ±1 standard deviation
- Significance testing: Student's t-test (p < 0.05)
- Curve fitting: Least squares regression
- Outlier detection: Grubbs test applied

## Calibration and Standards

### Gas Chromatography Calibration
- **Standard gases**: 100, 500, 1000, 5000 ppm H₂ in N₂
- **Calibration frequency**: Daily before measurements
- **Linearity**: R² > 0.999 required
- **Detection limit**: 10 ppm H₂

### Electrical Measurements
- **Voltage accuracy**: ±0.01% of reading
- **Current accuracy**: ±0.02% of reading
- **Calibration**: Annual traceable calibration
- **Resolution**: 0.1 mV, 0.1 mA

### Flow Measurements
- **Accuracy**: ±1% of full scale
- **Repeatability**: ±0.1% of reading
- **Calibration**: Semi-annual with NIST traceable standards

## Environmental Conditions

### Laboratory Environment
- **Temperature**: 23 ± 2°C
- **Humidity**: 45 ± 10% RH
- **Atmospheric pressure**: 1013 ± 10 mbar
- **Vibration isolation**: Optical table with pneumatic damping

### Safety Measures
- Hydrogen gas detector with 10% LEL alarm
- Fume hood operation for gas handling
- Emergency shut-off systems installed
- Personal protective equipment required

## Data Validation

### Reproducibility Tests
- Same experiment repeated on different days
- Different operators performing measurements
- Fresh electrode pairs for each validation
- Statistical comparison of results (ANOVA)

### Cross-Validation
- Alternative measurement methods where possible
- Literature comparison for known systems
- Mass balance verification (H₂ + O₂ production)
- Energy balance checks

## Limitations and Uncertainties

### Known Sources of Error
1. **Temperature fluctuations**: ±0.5°C → ±2% current variation
2. **Flow rate variations**: ±1% → ±0.5% efficiency change
3. **pH drift**: ±0.1 units → ±3% kinetic rate change
4. **Electrode aging**: <1% per hour of operation
5. **Gas sampling**: ±2% from dead volume effects

### Uncertainty Propagation
- Combined uncertainties calculated using RSS method
- Type A uncertainties from statistical analysis
- Type B uncertainties from equipment specifications
- Coverage factor k=2 for 95% confidence intervals

## Data Files Generated

1. `current_voltage_measurements.csv` - Main IV characteristic data
2. `hydrogen_production_rates.csv` - H₂ production and efficiency
3. `temperature_profiles.csv` - Temperature monitoring data
4. `efficiency_data.csv` - Energy efficiency calculations
5. `system_parameters.json` - Complete parameter set
6. `experimental_log.txt` - Detailed experimental notes

---

*For questions about experimental procedures or data interpretation, please refer to the corresponding author.*