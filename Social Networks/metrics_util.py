from random_person import famous_persons
import networkx as nx
import pandas as pd


def create_df(G):
    """
    This function creates a pandas DataFrame from a given networkx graph G.
    The DataFrame contains information about the top 100 nodes.

    Parameters:
    G (networkx.Graph): The input graph.

    Returns:
    pandas.DataFrame: A DataFrame with columns 'Name', 'Betweenness Centrality', 'Clustering Coefficient', and 'Degree'.
    """
    betweenness_centrality_list = calculate_betweenness_centrality(G)
    clustering_coefficient_list = calculate_clustering_coefficient(G)
    eigeness_centrality_list = get_eigenvector_centrality(G)
    degree_list = calculate_degree(G)
    load_centrality_list = get_load_centrality(G)

    df_md = pd.DataFrame({
        'Name': [person for person in famous_persons],
        'Betweenness Centrality': betweenness_centrality_list[:100],
        'Clustering Coefficient': clustering_coefficient_list[:100],
        'Degree': degree_list[:100],
        'Eigenvector Centrality': eigeness_centrality_list[:100],
        'Load Centrality': load_centrality_list[:100]

    })
    df_csv = pd.DataFrame({
        'Betweenness Centrality': betweenness_centrality_list,
        'Clustering Coefficient': clustering_coefficient_list,
        'Degree': degree_list,
        'Eigenvector Centrality': eigeness_centrality_list,
        'Load Centrality': load_centrality_list
    })
    return df_md, df_csv


def df_to_file(G):
    """
    This function generates a Markdown representation of a DataFrame containing information about the top 100 nodes
    in a given networkx graph G. The DataFrame is created by the `create_df` function. The Markdown string is then saved
    to a file named 'output.md'.

    Parameters:
    G (networkx.Graph): The input graph. This graph should contain nodes representing famous persons, and edges representing
                        relationships between them.

    Returns:
    None: The function does not return any value. It saves the Markdown string to a file.
    """
    df_md, df_csv = create_df(G)
    markdown_str = df_md.to_markdown(index=False)

    # Save the Markdown string to a file
    with open('output.md', 'w') as file:
        file.write(markdown_str)
    df_csv.to_csv('output.csv')

def calculate_betweenness_centrality(G):
    """
    Calculates the betweenness centrality of each node in the given networkx graph G.

    Betweenness centrality is a measure of a node's importance in a network. It quantifies how often a node acts as a bridge
    between other nodes in the network. Nodes with high betweenness centrality have a significant influence on the flow of
    information or resources in the network.

    Parameters:
    G (networkx.Graph): The input graph. This graph should contain nodes representing entities and edges representing
                        relationships between them.

    Returns:
    list: A list of floats representing the betweenness centrality of each node in the graph. The list is sorted in the same
          order as the nodes in the graph.
    """
    betweenness_centrality = nx.betweenness_centrality(G)
    betweenness_centrality_list = [bc for bc in betweenness_centrality.values()]
    return betweenness_centrality_list


def calculate_clustering_coefficient(G: object) -> list:
    """
    Calculates the clustering coefficient of each node in the given networkx graph G.

    Clustering coefficient is a measure of the degree to which nodes in a graph tend to cluster together. It quantifies
    the local density of connections in a network. A high clustering coefficient indicates that nodes in a graph tend to
    form tightly connected clusters.

    Parameters:
    G (networkx.Graph): The input graph. This graph should contain nodes representing entities and edges representing
                        relationships between them.

    Returns:
    list: A list of floats representing the clustering coefficient of each node in the graph. The list is sorted in the same
          order as the nodes in the graph.
    """
    clustering_coefficient = nx.clustering(G)
    clustering_coefficient_list = [cc for cc in clustering_coefficient.values()]
    return clustering_coefficient_list


# TODO: Add other metrics of centrality, such as eigenvector centrality or load centrality
def get_eigenvector_centrality(G):
    """
    Calculates the eigenvector centrality of each node in the given networkx graph G.

    Eigenvector centrality is a measure of the influence of a node in a network, quantified by the sum of the
    (weighted) connections to the node raised to the power of the eigenvalue. Nodes with high eigenvector centrality
    have a significant influence on the flow of information or resources in the network.

    Parameters:
    G (networkx.Graph): The input graph. This graph should contain nodes representing entities and edges representing
                        relationships between them.

    Returns:
    list: A list of floats representing the eigenvector centrality of each node in the graph. The list is sorted in the same
          order as the nodes in the graph.
    """
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter = 1000)
    eigenvector_centrality_list = [ec for ec in eigenvector_centrality.values()]
    return eigenvector_centrality_list


def get_load_centrality(G):
    """
        Calculates the load centrality of each node in the given networkx graph G.

        Load centrality is a measure of the influence of a node in a network, quantified by the sum of the in-degree
        and out-degree of the node divided by the total number of nodes in the network. Nodes with high load centrality
        have a significant influence on the flow of information or resources in the network.

        Parameters:
        G (networkx.Graph): The input graph. This graph should contain nodes representing entities and edges representing
                            relationships between them.

        Returns:
        list: A list of floats representing the load centrality of each node in the graph. The list is sorted in the same
              order as the nodes in the graph.
    """
    load_centrality = nx.load_centrality(G)
    load_centrality_list = [lc for lc in load_centrality.values()]
    return load_centrality_list


def calculate_degree(G):
    """
    Calculates the degree of each node in the given networkx graph G.

    Degree is a measure of the number of connections a node has in a network. Nodes with high degree have a significant
    influence on the flow of information or resources in the network.

    Parameters:
    G (networkx.Graph): The input graph. This graph should contain nodes representing entities and edges representing
                        relationships between them.

    Returns:
    list: A list of integers representing the degree of each node in the graph. The list is sorted in the same
          order as the nodes in the graph.
    """
    degree = nx.degree(G)
    degree_list = [d for d in degree]
    return degree_list
