import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pyvis.network import Network
import networkx as nx

# ----------------------- Importing dataframes -----------------------
nodes = pd.read_csv('../Dataset/Nodes.csv')
links = pd.read_csv('../Dataset/Links.csv')
# ---------------------------------------------------------------------

HEIGHT = 700
WIDTH = 700

st.header("VAST Challenge MC-1")
st.write("---")

# st.subheader("Dataset Description:")
'''
### Dataset Description:
  - Directed multi-graph: multiple edges between the same two nodes are possible.
  - Contains 3721 Nodes and 7422 Edges.
  - JSON format matches D3's node-link format (Compatible with networkx.nodelinkgraph).
  - The node entries must include a unique id key for each node.
  - The links entries include source and target keys that refer to node id values.   
---
'''

st.subheader("Nodes Dataframe")

'''
  - #### Node Attributes:
    - **Id**      : Identifier of the node is also usually the name of the entity. Some nodes have a numeric ID and do not have a name even if   they are a person, company, or organization.
    - **type**    : Type of the node as defined above. It is an optional attribute
    - **country** : Country associated with the entity. It is an optional attribute.
    - **dataset** : Always ‘MC1’
---
'''
# node choices
select_1, select_2, select_3 = st.columns(3)
type_unique = nodes["type"].unique()
type_choice = select_1.multiselect("Type:", type_unique)

country_unique = nodes["country"].unique()
country_choice = select_2.multiselect("Country:", country_unique)

id_unique = nodes["id"].unique()
id_choice = select_3.multiselect("ID:", id_unique)

filtered_nodes = nodes

if len(type_choice) == 0 and len(country_choice) == 0 and len(id_choice) == 0:
    n = st.data_editor(nodes, width=WIDTH)
elif len(type_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_nodes = nodes[nodes['type'].isin(type_choice)]

    n = st.data_editor(filtered_nodes, width=WIDTH)  # , width=WIDTH, height=HEIGHT
elif len(country_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_nodes = nodes[nodes['country'].isin(country_choice)]
    n = st.data_editor(filtered_nodes, width=WIDTH)  # , width=WIDTH, height=HEIGHT
elif len(id_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_nodes = nodes[nodes['id'].isin(id_choice)]
    n = st.data_editor(filtered_nodes, width=WIDTH)  # , width=WIDTH, height=HEIGHT

st.write("---")

st.subheader("Links Dataframe")
'''
  - #### Link Attributes:    
    - **source**  : ID of the source node
    - **target**  : ID of the target node
    - **type**    : Type of the edge as defined above. It is an optional attribute
    - **dataset** : Always ‘MC1’ 
    
---
'''
# link choices
select_l1, select_l2, select_l3, select_l4, select_l5 = st.columns(5)
type_unique = links["type"].unique()
type_choice = select_l1.multiselect("Type:", type_unique)

weight_unique = links["weight"].unique()
weight_choice = select_l2.multiselect("Weight:", weight_unique)

source_unique = links["source"].unique()
source_choice = select_l3.multiselect("Source:", source_unique)

target_unique = links["target"].unique()
target_choice = select_l4.multiselect("Destination:", target_unique)

key_unique = links["key"].unique()
key_choice = select_l5.multiselect("Key:", key_unique)
#
# filtered_liks = links
#
if len(type_choice) == 0 and len(weight_choice) == 0 and len(source_choice) == 0 \
        and len(target_choice) == 0 and len(key_choice) == 0:
    n = st.data_editor(links, width=WIDTH)

elif len(type_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_links = links[links['type'].isin(type_choice)]
    n = st.data_editor(filtered_links, width=WIDTH)  # , width=WIDTH, height=HEIGHT

elif len(weight_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_links = links[links['weight'].isin(weight_choice)]
    n = st.data_editor(filtered_links, width=WIDTH)  # , width=WIDTH, height=HEIGHT

elif len(source_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_links = links[links['source'].isin(source_choice)]
    n = st.data_editor(filtered_links, width=WIDTH) # , width=WIDTH, height=HEIGHT

elif len(target_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_links = links[links['target'].isin(target_choice)]
    n = st.data_editor(filtered_links, width=WIDTH)

elif len(key_choice) != 0:
    # get the filtered nodes from select boxes
    filtered_links = links[links['key'].isin(key_choice)]
    n = st.data_editor(filtered_links, width=WIDTH)


# creating the source to target charts
#---------------------------------------------


#---------------------------------------------

# ---------------------------------------- Test Purpose ----------------------------------------
# st.write("---")
# st.subheader("Pyvis Tutorial")
# nodes = [1, 2, 3, 4]
# labels = ['a', 'b', 'c', 'd']
#
# # first create a network
# net = Network(notebook=True, cdn_resources='remote', height="750px", width="100%", bgcolor="#20202b", font_color="white")
#
# # add_nodes() is used to add multiple nodes and labels from dataset
# net.add_nodes(nodes, label=labels)
# net.add_edge(1,2)
# net.add_edge(2,3)
# net.add_edge(3,4)
# net.add_edge(2,4)
# # net.add_edge(1,4)
#
# # allows for more fluid graph interactions
# #net.toggle_physics(True)
# # exporting the graph in .html
#
#
#
# # Save and read graph as HTML file (on Streamlit Sharing)
# try:
#    html_path = 'Helpers'
#    net.save_graph(f'{html_path}/pyvis_graph.html')
#    HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()
# # Save and read graph as HTML file (locally)
# except:
#     path = '/html_files'
#     net.save_graph(f'{html_path}/pyvis_graph.html')
#     HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()
#
# # Load HTML into HTML component for display on Streamlit
# components.html(HtmlFile, height=HEIGHT, width=WIDTH)

# ---------------------------------------- Test Purpose (end) ----------------------------------------
