# Mathematical Model

This document provides the complete mathematical formulation of the theoretical model used to analyze the membraneless electrolyzer.

## Governing Equations

### 1. Conservation of Mass
The steady-state conservation of mass for species $i$ in the electrolyte:

$$\nabla \cdot (\rho \mathbf{v}) = 0$$

where $\rho$ is the fluid density and $\mathbf{v}$ is the velocity vector.

### 2. Species Transport
The transport of ionic species is governed by the Nernst-Planck equation:

$$\nabla \cdot \mathbf{N}_i = R_i$$

where the molar flux $\mathbf{N}_i$ is given by:

$$\mathbf{N}_i = -D_i \nabla c_i - \frac{z_i F D_i c_i}{RT} \nabla \phi + c_i \mathbf{v}$$

**Variables:**
- $c_i$: concentration of species $i$ (mol/m³)
- $D_i$: diffusion coefficient of species $i$ (m²/s)
- $z_i$: charge number of species $i$
- $F$: Faraday constant (96,485 C/mol)
- $R$: universal gas constant (8.314 J/mol·K)
- $T$: temperature (K)
- $\phi$: electric potential (V)
- $R_i$: reaction rate of species $i$ (mol/m³·s)

### 3. Momentum Conservation
The fluid flow is described by the Navier-Stokes equations:

$$\rho (\mathbf{v} \cdot \nabla) \mathbf{v} = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}$$

where:
- $p$: pressure (Pa)
- $\mu$: dynamic viscosity (Pa·s)
- $\mathbf{f}$: body forces (N/m³)

### 4. Electroneutrality
The electroneutrality condition must be satisfied:

$$\sum_i z_i c_i = 0$$

### 5. Electric Potential
The electric potential distribution follows Laplace's equation in the bulk electrolyte:

$$\nabla^2 \phi = 0$$

## Electrochemical Reactions

### Anodic Reaction (Oxygen Evolution)
$$2 H_2O \rightarrow O_2 + 4 H^+ + 4 e^-$$

**Butler-Volmer kinetics:**
$$i_a = i_{0,a} \left[ \exp\left(\frac{\alpha_a F \eta_a}{RT}\right) - \exp\left(-\frac{(1-\alpha_a) F \eta_a}{RT}\right) \right]$$

### Cathodic Reaction (Hydrogen Evolution)
$$2 H^+ + 2 e^- \rightarrow H_2$$

**Butler-Volmer kinetics:**
$$i_c = i_{0,c} \left[ \exp\left(\frac{\alpha_c F \eta_c}{RT}\right) - \exp\left(-\frac{(1-\alpha_c) F \eta_c}{RT}\right) \right]$$

**Variables:**
- $i_{0,a}$, $i_{0,c}$: exchange current densities (A/m²)
- $\alpha_a$, $\alpha_c$: charge transfer coefficients
- $\eta_a$, $\eta_c$: overpotentials (V)

## Boundary Conditions

### 1. Electrode Surfaces
At the anode surface ($z = 0$):
$$-\mathbf{n} \cdot \mathbf{N}_{H^+} = \frac{i_a}{F}$$
$$-\mathbf{n} \cdot \mathbf{N}_{O_2} = -\frac{i_a}{4F}$$

At the cathode surface ($z = L$):
$$-\mathbf{n} \cdot \mathbf{N}_{H^+} = -\frac{i_c}{F}$$
$$-\mathbf{n} \cdot \mathbf{N}_{H_2} = \frac{i_c}{2F}$$

### 2. Inlet Conditions
At the inlet ($x = 0$):
$$c_i = c_{i,inlet}$$
$$\mathbf{v} = \mathbf{v}_{inlet}$$

### 3. Outlet Conditions
At the outlet ($x = L_{channel}$):
$$\frac{\partial c_i}{\partial x} = 0$$
$$\frac{\partial \mathbf{v}}{\partial x} = 0$$

### 4. Wall Conditions
At solid walls:
$$\mathbf{v} = 0$$ (no-slip condition)
$$\mathbf{n} \cdot \mathbf{N}_i = 0$$ (no flux condition)

## Performance Metrics

### 1. Current Density
$$j = \frac{I}{A_{electrode}}$$

where $I$ is the total current and $A_{electrode}$ is the electrode area.

### 2. Hydrogen Production Rate
$$\dot{n}_{H_2} = \frac{I}{2F}$$

### 3. Energy Efficiency
$$\eta_{energy} = \frac{\Delta H_{H_2} \cdot \dot{n}_{H_2}}{V \cdot I}$$

where $\Delta H_{H_2} = 286$ kJ/mol is the enthalpy of formation of hydrogen.

### 4. Voltage Efficiency
$$\eta_{voltage} = \frac{V_{theoretical}}{V_{cell}}$$

where $V_{theoretical} = 1.229$ V is the theoretical decomposition voltage.

## Dimensionless Groups

### 1. Reynolds Number
$$Re = \frac{\rho v L}{\mu}$$

### 2. Schmidt Number
$$Sc = \frac{\mu}{\rho D}$$

### 3. Péclet Number
$$Pe = \frac{v L}{D}$$

### 4. Damköhler Number
$$Da = \frac{k L}{v}$$

where $k$ is a characteristic reaction rate constant.

## Numerical Implementation

The coupled system of equations is solved using:
- Finite element method for spatial discretization
- Implicit time stepping for transient problems
- Newton-Raphson method for nonlinear iterations
- GMRES solver for linear systems

### Convergence Criteria
- Residual tolerance: $10^{-6}$
- Maximum iterations: 50
- Mesh independence verified with refinement studies