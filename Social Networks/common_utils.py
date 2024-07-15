import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
#fig2, ax = plt.subplots(1, 1, figsize=(30, 30))
fig, axs = plt.subplots(1, 2)


def plt_metrics(susceptible_counts, infected_counts, recovered_counts, perm_immune_counts, G, pos, t):
    """
    This function is responsible for visualizing the SIR model simulation on a network graph and updating the metrics plot.

    Parameters:
    susceptible_counts (list): A list containing the number of susceptible individuals at each time step.
    infected_counts (list): A list containing the number of infected individuals at each time step.
    recovered_counts (list): A list containing the number of recovered individuals at each time step.
    perm_immune_counts (list): A list containing the number of permanently immune individuals at each time step.
    G (networkx.Graph): The network graph representing the social network. The graph should have node attributes 'state' which can be one of the following: 'S' (Susceptible), 'I' (Infected), or 'R' (Recovered).
    pos (dict): A dictionary containing the positions of the nodes in the network graph.
    t (int): The current time step.

    Returns:
    None. The function updates the matplotlib figures and pauses for 0.1 seconds.
    """

    node_colors = [get_node_color(G.nodes[node]['state']) for node in G.nodes]

    # Draw newtwork graph
    #nx.draw(G, pos, node_color=np.array(node_colors), with_labels=True, node_size=500, font_color='white', ax=ax)
    #ax.set_title(f'Timestep {t}')
    labelstr = '\n'.join((
        "Blue: Susceptible",
        "Red: Infected",
        "Green: Recovered",
        "Yellow: Permanently Immune",
    ))
    # set text at top right corner of figure
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    #ax.text(0.95, 0.05, labelstr, transform= ax.transAxes, fontsize=10)
    axs[0].cla()
    axs[0].axis('off')
    textstr = '\n'.join((
        f'Susceptible: {susceptible_counts[-1]:,d}',
        f'Infected: {infected_counts[-1]:,d}',
        f'Recovered: {recovered_counts[-1]:,d}',
        f'Permanently Immune: {perm_immune_counts[-1]:,d}',
        f'Average Degree of Infected: {avg_degree_infected(G):.2f}',
    ))
    axs[0].text(0.5, 0.5, textstr, transform=axs[0].transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='center', bbox=props)

    axs[1].clear()
    axs[1].plot(susceptible_counts, label='Susceptible', color="blue")
    axs[1].plot(infected_counts, label='Infected', color="red")
    axs[1].plot(recovered_counts, label='Recovered', color="green")
    axs[1].plot(perm_immune_counts, label='Immune', color="yellow")
    axs[1].set_xlabel('Time Steps')
    axs[1].set_ylabel('Number of Individuals')
    axs[1].legend()
    axs[1].set_title("Watts Strogatz Model SIR Simulation")
    plt.tight_layout()
    plt.pause(0.1)
    # if t == 99:
    #    fig.savefig('watts_strogatz_model_output.png')
    #    fig2.savefig('watts_strogatz_model_metrics.png')

def get_node_color(state):
    """
    This function returns the color corresponding to the given state of an individual node in the SIR model.

    Parameters:
    state (str): The state of the individual node. It can be one of the following: 'S' (Susceptible), 'I' (Infected), or 'R' (Recovered).

    Returns:
    str: The color corresponding to the given state. It can be one of the following: 'blue' for 'S', 'red' for 'I', or 'green' for 'R'.
    """
    return {
        'S': 'blue',
        'I': 'red',
        'R': 'green',
        'P': 'yellow'  # perm immune
    }[state]


def get_node_metrics(G):
    """
    This function calculates and returns the lists of susceptible, infected, and recovered nodes in the given network graph.

    Parameters:
    G (networkx.Graph): The network graph representing the social network. The graph should have node attributes 'state' which can be one of the following: 'S' (Susceptible), 'I' (Infected), or 'R' (Recovered).

    Returns:
    tuple: A tuple containing four lists: susceptible nodes, infected nodes, recovered nodes, and perm_immune nodes.
    """
    susceptible = [node for node in G.nodes if G.nodes[node]['state'] == 'S']
    infected = [node for node in G.nodes if G.nodes[node]['state'] == 'I']
    recovered = [node for node in G.nodes if G.nodes[node]['state'] == 'R']
    perm_immune = [node for node in G.nodes if G.nodes[node]['state'] == 'P']
    return susceptible, infected, recovered, perm_immune


def avg_degree_infected(G):
    tup_degree = nx.degree(G)
    avg_degree_infected = sum([tup_degree[node] for node in G.nodes if G.nodes[node]['state'] == 'I']) / len(
        [tup_degree[node] for node in G.nodes if G.nodes[node]['state'] == 'I'])
    return avg_degree_infected


def change_degree_type(deg):
    """
    This function takes a degree value as a string, removes any leading or trailing whitespaces, and removes parentheses,
    then converts the last two characters of the resulting string to a numeric value.

    Parameters:
    deg (str): A string representing a degree value. The string should be in the format "(xx)" where "xx" is a two-digit number.

    Returns:
    int: The numeric value of the last two characters of the input string after removing leading/trailing whitespaces and parentheses.
    """
    deg = deg.strip()
    deg = deg.strip("()")
    return pd.to_numeric(deg[-2:])
