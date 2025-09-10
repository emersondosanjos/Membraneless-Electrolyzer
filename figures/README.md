# Figures Directory

This directory contains additional figures and visualizations that supplement the main manuscript.

## Structure

```
figures/
├── main/              # Figures included in the main paper
├── supplementary/     # Additional figures for supplementary material
├── raw/               # Raw figure files before processing
└── scripts/           # Figure generation scripts
```

## Figure Categories

### Main Manuscript Figures
- **`fig1_schematic.pdf`**: Schematic diagram of the membraneless electrolyzer
- **`fig2_iv_curves.pdf`**: Current-voltage characteristic curves
- **`fig3_hydrogen_production.pdf`**: Hydrogen production rate analysis
- **`fig4_efficiency.pdf`**: Energy efficiency comparison
- **`fig5_parametric_study.pdf`**: Parametric sensitivity analysis

### Supplementary Figures
- **`figS1_experimental_setup.pdf`**: Detailed experimental setup
- **`figS2_mass_transport.pdf`**: Mass transport visualization
- **`figS3_temperature_profiles.pdf`**: Temperature distribution analysis
- **`figS4_uncertainty_analysis.pdf`**: Error bars and uncertainty quantification
- **`figS5_comparison_literature.pdf`**: Comparison with literature data

### Additional Visualizations
- **`concentration_profiles.pdf`**: Concentration gradients visualization
- **`velocity_fields.pdf`**: Flow field analysis
- **`performance_maps.pdf`**: Operating condition maps

## Figure Generation

All figures can be regenerated using the scripts in the `../code/plotting/` directory:

```python
# Example: Generate main figures
python ../code/plotting/figure_generation.py --figure all
python ../code/plotting/supplementary_plots.py --output supplementary/
```

## Format Standards

- All figures are provided in PDF format for high-quality reproduction
- Vector graphics are used where appropriate for scalability
- Color schemes are colorblind-friendly and print-ready
- Font sizes and styles are consistent with journal requirements

## Copyright

All figures are the original work of the authors and are made available under the terms of the MIT License (see LICENSE file).