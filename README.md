# 🦠 Stochastic Network Contagion: SIR Dynamics on Scale-Free Graphs

![Status](https://img.shields.io/badge/Status-Research_Complete-success?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-Network_Science_&_Epidemiology-blueviolet?style=for-the-badge)
![Language](https://img.shields.io/badge/Stack-Python_|_NetworkX_|_NumPy-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> **A Monte Carlo simulation** modeling the propagation of infectious agents through heterogeneous social networks. This project investigates how network topology (specifically "Hub" nodes) accelerates viral diffusion compared to standard compartmental models.

---

## 🔭 Abstract

Traditional epidemiological models (like deterministic SIR) assume a "well-mixed" population where every individual has an equal probability of contacting everyone else. However, real-world human networks are **Scale-Free**, meaning a small number of individuals ("Super-Spreaders") possess a disproportionately high number of connections.

This repository implements a **Stochastic SIR Model** on a **Barabási–Albert (BA) Graph** to simulate realistic outbreak kinetics. The results demonstrate the critical role of network topology in the initial exponential growth phase of a pandemic.

---

## 🧮 Mathematical Framework

### 1. Network Topology (The Environment)
The population structure is generated using the **Barabási–Albert algorithm**, which constructs a scale-free network via *Preferential Attachment*.
The probability $P(k)$ that a node in the network interacts with $k$ other nodes follows a power-law distribution:

$$P(k) \sim k^{-3}$$

This ensures the emergence of "Hubs"—nodes with degrees orders of magnitude higher than the average, mimicking real-world social super-connectors.

### 2. Viral Dynamics (The Agent)
We implement a discrete-time Markovian process for the **Susceptible-Infected-Recovered (SIR)** progression:

* **Transmission ($\beta$):** A Susceptible node $i$ becomes Infected with probability $P_{inf}$ based on its neighbors:
    $$P(S_i \to I_i) = 1 - (1 - \beta)^{n_{inf}}$$
    *Where $\beta$ is the infection rate per contact and $n_{inf}$ is the number of infected neighbors.*

* **Recovery ($\gamma$):** An Infected node recovers with a fixed probability per time step:
    $$P(I_i \to R_i) = \gamma$$

### 3. Basic Reproduction Number ($R_0$)
The effective reproduction number for this simulation is calculated as:
$$R_0 = \frac{\beta}{\gamma} = \frac{0.3}{0.05} = 6.0$$
*An $R_0$ of 6.0 indicates a highly contagious pathogen, comparable to the Measles virus or the Delta variant of SARS-CoV-2.*

---

## 💻 Simulation Parameters

The simulation is configured with the following hyperparameters to model a dense, rapid outbreak scenario:

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Population ($N$)** | 1,000 | Total nodes in the graph |
| **Connectivity ($m$)** | 3 | Edges attached per new node (BA Model) |
| **Infection Rate ($\beta$)** | 0.30 | Probability of transmission per contact |
| **Recovery Rate ($\gamma$)** | 0.05 | Probability of recovery per step |
| **Time Steps ($t$)** | 50 | Duration of the simulation (Days) |

---

## 📉 Simulation Results

The visualization below captures the system state dynamics.
* **Left Panel:** The classic epidemiological curves. Note the rapid depletion of the Susceptible pool (Blue) due to the high $R_0$.
* **Right Panel:** A topological snapshot showing the virus clustering around high-degree nodes.

![Epidemic Report](epidemic_report.png)

*Observations:* The "Infected" curve (Red) peaks at approx. $t=15$, creating a massive burden on the system before herd immunity (Green) is established.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.8+
* `pip` package manager

### 1. Clone the Repository
```bash
git clone https://github.com/PradyumnShirsath/stochastic-network-contagion.git
cd stochastic-network-contagion

🔮 Future Roadmap
Percolation Analysis: Determine the critical node removal threshold to shatter the network (Vaccination Strategy).

SEIR Model: Introduce an "Exposed" (latent) period for higher fidelity.

Dynamic Graphs: Allow edges to break/form over time (Simulating Quarantine/Social Distancing).

<div align="center">

Author: Pradyumn Shirsath Researching Complex Systems, Network Dynamics & AI Safety

</div>