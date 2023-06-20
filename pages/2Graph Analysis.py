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
nodes = pd.read_csv("Dataset/Nodes.csv")

# Streamlit code
st.title('Knowledge Graph Analysis')
st.divider()

# create three columns
a, b = st.columns(2)
d, e = st.columns(2, gap="large")

choice = e.checkbox("Turn on animations:")

es = ['dynamic', 'continuous', 'discrete', 'diagonalCross', 'straightCross',
      'horizontal', 'vertical', 'curvedCW', 'curvedCCW', 'cubicBezier']
edge_smooth = d.selectbox("Select Edge Smooth Algorithm:", es)

# st.divider()

# Entities to investigate
entities_to_investigate = ['Mar de la Vida OJSC', '979893388',
                           'Oceanfront Oasis Inc Carriers', '8327']
eti_choice = a.multiselect("Select one or more suspected entities to investigate:", entities_to_investigate)
# getting unique nodes
entities = nodes["id"]
eti2_choice = b.multiselect("Select one or more nodes to investigate:", entities)

# adding suspected entitites with remaining selected nodes
eti_choice = list(set(eti2_choice) - set(eti_choice)) + eti_choice

st.divider()
# Slider for confidence score threshold
conf_threshold = st.slider('Weight threshold', min_value=0.0000, max_value=1.0, value=0.028, step=0.0001)
st.divider()

# ----------------------------------- Pyvis Setting -----------------------------------
# Create Pyvis network
net = Network(notebook=True,  directed=True, height=str(HEIGHT)+"px",
              width="100%", filter_menu=False, select_menu=False, cdn_resources='remote')

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
graph = nx.from_pandas_edgelist(df, 'source', 'target', edge_key='type',
                            edge_attr='weight', create_using=graph_type)

nodes_of_interest = set(eti_choice)

source_list = []
target_list = []
edge_type_list = []

# Find all nodes connected to entities of interest
for entity in eti_choice:
    if entity in graph:
        for neighbor in graph[entity]:
            edge_data = graph.get_edge_data(entity, neighbor)
            for edge_type, edge_values in edge_data.items():
                if 'weight' in edge_values and edge_values['weight'] >= conf_threshold:
                    # st.write(f"[ {entity} ---->   {neighbor} ] ====> Type: {edge_type}")
                    source_list.append(entity)
                    target_list.append(neighbor)
                    edge_type_list.append(edge_type)
                    nodes_of_interest.add(neighbor)

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
components.html(source_code, height = HEIGHT, width=WIDTH+70)
# ----------------------------------- Saving Graph -----------------------------------

# showing relation between source and target nodes
graph_dict = {'Source':source_list, 'Relation':edge_type_list, 'Target':target_list}

graph_df = pd.DataFrame(graph_dict)
st.dataframe(graph_df, width=WIDTH+200, hide_index=True)