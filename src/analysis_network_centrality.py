'''
PART 1: NETWORK CENTRALITY METRICS

Using the imbd_movies dataset
- Guild a graph and perform some rudimentary graph analysis, extracting centrality metrics from it. 
- Below is some basic code scaffolding that you will need to add to. 
- Tailor this code scaffolding and its stucture to however works to answer the problem
- Make sure the code is line with the standards we're using in this class 
'''

import numpy as np
import pandas as pd
import networkx as nx

# Build the graph
g = nx.Graph()
edges = []

# Set up your dataframe(s) -> the df that's output to a CSV should include at least the columns 'left_actor_name', '<->', 'right_actor_name'

with open(filepath, 'r') as in_file:
    # Don't forget to comment your code
    for line in in_file:
        # Don't forget to include docstrings for all functions

        # Load the movie from this line
        this_movie = json.loads(line)
            
        # Create a node for every actor
        for actor_id,actor_name in this_movie['actors']:
        # add the actor to the graph    
            g.add_node(actor_name)
        # Iterate through the list of actors, generating all pairs
        ## Starting with the first actor in the list, generate pairs with all subsequent actors
        ## then continue to second actor in the list and repeat
        
        i = 0 #counter
        for left_actor_id,left_actor_name in this_movie['actors']:
            for right_actor_id,right_actor_name in this_movie['actors'][i+1:]:

                # Get the current weight, if it exists
                if g.has_edge(left_actor_name, right_actor_name):
                        # If the edge exists, increment its weight by 1
                        g[left_actor_name][right_actor_name]['weight'] += 1
                else:
                    # If the edge doesn't exist, add a new edge with weight 1
                    g.add_edge(left_actor_name, right_actor_name, weight=1)
            
                # Add an edge for these actors
                edges.append([left_actor_name, '<->', right_actor_name])

            i += 1 
   
df = pd.DataFrame(edges, columns=['left_actor_name', '<->', 'right_actor_name'])


# Print the info below
print("Nodes:", len(g.nodes))

#Print the 10 the most central nodes
centrality = nx.degree_centrality(g)
most_central = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 most central nodes:")
for node, cent in most_central:
    print(f"{g.nodes[node]['name']} (ID: {node}): {cent}")

# Output the final dataframe to a CSV named 'network_centrality_{current_datetime}.csv' to `/data`
