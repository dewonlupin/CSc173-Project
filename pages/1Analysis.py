import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
import math


HEIGHT = 1000
WIDTH = 850


# Load the data
df = pd.read_csv("Dataset/Links.csv")

# Streamlit code
st.title('Knowledge Graph Analysis')
st.divider()
# create three columns
a, b, c = st.columns(3)

# Slider for confidence score threshold
conf_threshold = b.slider('Weight threshold', min_value=0.0, max_value=1.0, value=0.28, step=0.001)

choice = c.checkbox("Turn on animations:")

es = ['dynamic', 'continuous', 'discrete', 'diagonalCross', 'straightCross',
      'horizontal', 'vertical', 'curvedCW', 'curvedCCW', 'cubicBezier']
edge_smooth = c.selectbox("Select Edge Smooth Algorithm:", es)

st.divider()


# Entities to investigate
entities_to_investigate = ['Mar de la Vida OJSC', '979893388',
                           'Oceanfront Oasis Inc Carriers', '8327']
eti_choice = a.multiselect("Select one or more entities to investigate:", entities_to_investigate)

# ----------------------------------- Pyvis Setting -----------------------------------
# Create Pyvis network
net = Network(notebook=True,  directed=True, height=str(HEIGHT)+"px",
              width="100%", filter_menu=False, select_menu=False)

# toggling physics value
if choice:
    net.toggle_physics(True)
else:
    net.toggle_physics(False)

# assigning edge smooth algorithm
net.set_edge_smooth(edge_smooth)
net.force_atlas_2based(gravity=-10, central_gravity=0.001,
                       spring_length=200, spring_strength=0.01,
                       damping=2, overlap=0)
# ----------------------------------- Pyvis Setting -----------------------------------

# ----------------------------------- main Graph logic -----------------------------------
# Create the graph
graph_type = nx.MultiDiGraph()
graph = nx.from_pandas_edgelist(df, 'source', 'target', edge_key='key',
                            edge_attr=True, create_using=graph_type)

# Find all nodes connected to entities of interest
nodes_of_interest = set(eti_choice)
for entity in eti_choice:
    if entity in graph:
        nodes_of_interest.update(graph.neighbors(entity))

# Create subgraph with nodes of interest
sub_graph = graph.subgraph(nodes_of_interest)

# converting nx_graph to pyvis_graph
net.from_nx(sub_graph)

# ----------------------------------- main Graph logic -----------------------------------

# ----------------------------------- Graph Coloring logic -----------------------------------
node_colors = {
    'Mar de la Vida OJSC': 'blue',
    '979893388': '#FF5335',
    'Oceanfront Oasis Inc Carriers': '#8458B3',
    '8327': 'purple'
}

for node in net.nodes:
    # Assign color based on position in list
    if node['id'] in node_colors:
        node['color'] = node_colors[node['id']]
    else:
        # node color for all nodes apart from entities_to_investigate
        node['color'] = '#E4F9F5'
    # assigning the radius of nodes according to node's neighbour count
    node['value'] = 5 * math.log(len(sub_graph[node['id']]) + 1)
# ----------------------------------- Graph Coloring logic -----------------------------------

# ----------------------------------- Saving Graph -----------------------------------
# Save to html and serve up the HTML
html_file = 'temp_graph.html'
net.save_graph(html_file)

# Display the graph
HtmlFile = open(html_file, 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height = HEIGHT, width=WIDTH)
# ----------------------------------- Saving Graph -----------------------------------
