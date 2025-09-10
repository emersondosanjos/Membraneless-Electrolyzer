# Nomenclature and Symbol Definitions

This document provides a comprehensive list of all symbols, variables, and constants used throughout the research.

## Roman Letters

| Symbol | Description | Units | Notes |
|--------|-------------|-------|--------|
| $A$ | Electrode area | m² | Active surface area |
| $c_i$ | Concentration of species $i$ | mol/m³ | Molar concentration |
| $D_i$ | Diffusion coefficient of species $i$ | m²/s | Temperature dependent |
| $F$ | Faraday constant | C/mol | 96,485.3329 C/mol |
| $I$ | Current | A | Total cell current |
| $i$ | Current density | A/m² | Current per unit area |
| $i_0$ | Exchange current density | A/m² | Kinetic parameter |
| $j$ | Current density | A/m² | Alternative notation |
| $k$ | Reaction rate constant | Various | Depends on reaction order |
| $L$ | Characteristic length | m | Channel length or width |
| $\mathbf{N}_i$ | Molar flux of species $i$ | mol/m²·s | Vector quantity |
| $p$ | Pressure | Pa | Fluid pressure |
| $R$ | Universal gas constant | J/mol·K | 8.3144598 J/mol·K |
| $R_i$ | Reaction rate of species $i$ | mol/m³·s | Source/sink term |
| $T$ | Temperature | K | Absolute temperature |
| $t$ | Time | s | Temporal coordinate |
| $V$ | Voltage | V | Cell voltage |
| $\mathbf{v}$ | Velocity vector | m/s | Fluid velocity |
| $x, y, z$ | Spatial coordinates | m | Cartesian coordinates |

## Greek Letters

| Symbol | Description | Units | Notes |
|--------|-------------|-------|--------|
| $\alpha$ | Charge transfer coefficient | - | 0 ≤ α ≤ 1 |
| $\eta$ | Overpotential | V | $\eta = \phi - \phi_{eq}$ |
| $\phi$ | Electric potential | V | Electrostatic potential |
| $\rho$ | Density | kg/m³ | Fluid density |
| $\mu$ | Dynamic viscosity | Pa·s | Fluid viscosity |
| $\sigma$ | Conductivity | S/m | Electrical conductivity |
| $\tau$ | Time constant | s | Characteristic time |
| $\omega$ | Angular frequency | rad/s | For AC analysis |

## Subscripts and Superscripts

### Subscripts
- $a$ : Anode
- $c$ : Cathode  
- $eq$ : Equilibrium
- $i$ : Species index
- $in$ : Inlet
- $out$ : Outlet
- $ref$ : Reference state
- $0$ : Initial or standard conditions

### Superscripts
- $*$ : Dimensionless quantity
- $n$ : Time level (for numerical schemes)
- $T$ : Transpose (for matrices)

## Dimensionless Numbers

| Symbol | Description | Definition | Physical Significance |
|--------|-------------|------------|----------------------|
| $Re$ | Reynolds number | $\frac{\rho v L}{\mu}$ | Inertial vs viscous forces |
| $Sc$ | Schmidt number | $\frac{\mu}{\rho D}$ | Momentum vs mass diffusion |
| $Pe$ | Péclet number | $\frac{v L}{D}$ | Convection vs diffusion |
| $Da$ | Damköhler number | $\frac{k L}{v}$ | Reaction vs transport |
| $Sh$ | Sherwood number | $\frac{k_m L}{D}$ | Mass transfer enhancement |
| $Nu$ | Nusselt number | $\frac{h L}{k_{th}}$ | Heat transfer enhancement |

## Chemical Species

| Symbol | Description | Molecular Weight (g/mol) |
|--------|-------------|--------------------------|
| $H^+$ | Proton (hydronium ion) | 1.008 |
| $OH^-$ | Hydroxide ion | 17.007 |
| $H_2O$ | Water | 18.015 |
| $H_2$ | Hydrogen gas | 2.016 |
| $O_2$ | Oxygen gas | 31.998 |
| $Na^+$ | Sodium ion | 22.990 |
| $Cl^-$ | Chloride ion | 35.453 |

## Standard Conditions

| Parameter | Symbol | Value | Units |
|-----------|---------|-------|-------|
| Standard temperature | $T_{std}$ | 298.15 | K |
| Standard pressure | $p_{std}$ | 101,325 | Pa |
| Standard hydrogen electrode | $\phi_{SHE}$ | 0.000 | V |
| Standard oxygen potential | $\phi_{O_2/H_2O}$ | 1.229 | V |
| Theoretical decomposition voltage | $V_{th}$ | 1.229 | V |

## Material Properties (at 25°C)

| Property | Symbol | Value | Units |
|----------|---------|-------|-------|
| Water density | $\rho_{H_2O}$ | 997.0 | kg/m³ |
| Water viscosity | $\mu_{H_2O}$ | 8.9×10⁻⁴ | Pa·s |
| H⁺ diffusivity | $D_{H^+}$ | 9.31×10⁻⁹ | m²/s |
| OH⁻ diffusivity | $D_{OH^-}$ | 5.27×10⁻⁹ | m²/s |
| H₂ diffusivity | $D_{H_2}$ | 4.5×10⁻⁹ | m²/s |
| O₂ diffusivity | $D_{O_2}$ | 2.0×10⁻⁹ | m²/s |

## Abbreviations

- **SHE**: Standard Hydrogen Electrode
- **OER**: Oxygen Evolution Reaction
- **HER**: Hydrogen Evolution Reaction
- **IV**: Current-Voltage
- **CFD**: Computational Fluid Dynamics
- **FEM**: Finite Element Method
- **PDE**: Partial Differential Equation
- **BV**: Butler-Volmer
- **NP**: Nernst-Planck

## Conversion Factors

| From | To | Factor |
|------|-----|--------|
| A/cm² | A/m² | 10,000 |
| mV | V | 0.001 |
| mmol/s | mol/s | 0.001 |
| mL/min | m³/s | 1.667×10⁻⁸ |
| °C | K | +273.15 |
| bar | Pa | 100,000 |

## Notes

1. All potentials are referenced to the Standard Hydrogen Electrode (SHE) unless otherwise noted.
2. Concentrations are given in molar units (mol/L or mol/m³) unless specified.
3. Standard conditions refer to 25°C and 1 atm pressure.
4. Diffusion coefficients are for infinite dilution in water at 25°C.
5. Current density is based on geometric (projected) electrode area unless noted as specific surface area.