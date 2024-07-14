from random_person import famous_persons
import networkx as nx
import pandas as pd

def create_df(G):
    betweenness_centrality_list = calculate_betweenness_centrality(G)
    clustering_coefficient_list = calculate_clustering_coefficient(G)
    df = pd.DataFrame({
        'Name': [person for person in famous_persons],
        'Betweenness Centrality': betweenness_centrality_list[:100],
        'Clustering Coefficient': clustering_coefficient_list[:100],
        'Degree': [G.degree(person) for person in range(100)]
    })
    ## Make a copy of the Dataframe with the first 100 rows
    return df

def df_to_md(G):
    df = create_df(G)
    markdown_str = df.to_markdown(index=False)

    # Save the Markdown string to a file
    with open('output.md', 'w') as file:
        file.write(markdown_str)

def calculate_betweenness_centrality(G):
    betweenness_centrality = nx.betweenness_centrality(G)
    betweenness_centrality_list = [bc for bc in betweenness_centrality.values()]
    return betweenness_centrality_list

def calculate_clustering_coefficient(G):
    clustering_coefficient = nx.clustering(G)
    clustering_coefficient_list = [cc for cc in clustering_coefficient.values()]
    return clustering_coefficient_list