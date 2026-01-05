import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# --- 1. CONFIGURATION ---
POPULATION = 1000        # Number of people (Nodes)
CONNECTIONS = 3          # Average friends per person
INFECTION_RATE = 0.3     # Probability of spreading (Beta)
RECOVERY_RATE = 0.05     # Probability of recovering (Gamma)
STEPS = 50               # How long to run the simulation

def run_simulation():
    print("🔬 Initializing Social Network Topology (Barabási–Albert Model)...")
    
    # Generate a "Scale-Free" Graph (Realistic social network structure)
    G = nx.barabasi_albert_graph(POPULATION, CONNECTIONS)
    
    # Set everyone to 'Susceptible' (Healthy)
    nx.set_node_attributes(G, 'Susceptible', 'status')
    
    # Patient Zero: Infect one random person
    patient_zero = random.choice(list(G.nodes()))
    G.nodes[patient_zero]['status'] = 'Infected'
    
    history = {'S': [], 'I': [], 'R': []}
    print(f"⚠️ Outbreak started at Node {patient_zero}. Simulating {STEPS} days...")

    # --- 2. THE SIMULATION LOOP ---
    for t in range(STEPS):
        # Snapshot current state
        statuses = list(nx.get_node_attributes(G, 'status').values())
        history['S'].append(statuses.count('Susceptible'))
        history['I'].append(statuses.count('Infected'))
        history['R'].append(statuses.count('Recovered'))
        
        # Find all currently infected nodes
        infected_nodes = [n for n, s in G.nodes(data='status') if s == 'Infected']
        
        # Spread Logic
        new_infections = []
        new_recoveries = []
        
        for node in infected_nodes:
            # Try to infect neighbors
            for neighbor in G.neighbors(node):
                if G.nodes[neighbor]['status'] == 'Susceptible':
                    if random.random() < INFECTION_RATE:
                        new_infections.append(neighbor)
            
            # Try to recover yourself
            if random.random() < RECOVERY_RATE:
                new_recoveries.append(node)
                
        # Update States
        for n in new_infections:
            G.nodes[n]['status'] = 'Infected'
        for n in new_recoveries:
            G.nodes[n]['status'] = 'Recovered'

    print("✅ Simulation Complete.")
    return history, G

def plot_results(history, G):
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: The SIR Curves
    ax1.plot(history['S'], label='Susceptible', color='#00D4FF') # Blue
    ax1.plot(history['I'], label='Infected', color='#FF3D00')    # Red
    ax1.plot(history['R'], label='Recovered', color='#00E676')   # Green
    ax1.set_title("SIR Epidemic Curves", fontweight='bold')
    ax1.set_xlabel("Time (Days)")
    ax1.set_ylabel("Population")
    ax1.legend()
    ax1.grid(alpha=0.2)
    
    # Plot 2: Network Topology Sample (First 100 nodes for visibility)
    subgraph = G.subgraph(list(G.nodes())[:100])
    pos = nx.spring_layout(subgraph, seed=42)
    
    # Color mapping
    color_map = []
    for node in subgraph:
        status = subgraph.nodes[node]['status']
        if status == 'Susceptible': color_map.append('#00D4FF')
        elif status == 'Infected': color_map.append('#FF3D00')
        else: color_map.append('#00E676')
        
    nx.draw(subgraph, pos, ax=ax2, node_color=color_map, node_size=50, edge_color='white', alpha=0.6)
    ax2.set_title("Network Topology Impact (Sample)", fontweight='bold')
    
    plt.savefig('epidemic_report.png', dpi=300)
    print("📸 Visual report saved to epidemic_report.png")
    plt.show()

if __name__ == "__main__":
    history, G = run_simulation()
    plot_results(history, G)