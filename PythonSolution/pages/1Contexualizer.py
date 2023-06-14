"""
This is the first question of VAST Mini Challenge-1
"""
from pyvis.network import Network

import streamlit as st
import streamlit.components.v1 as components

import pandas as pd

HEIGHT = 1000
WIDTH = 850

st.header("Contexualizer")
st.subheader("Mini Challenge Question-1")
st.divider()
st.write("Use visual analytics to dynamically display and explore context around the suspected entities listed above. "
         "What did you learn about each one? Can you connect them to illegal fishing? "
         "Provide evidence for or against the case that each entity is involved in illegal fishing and use visual analytics"
         " to express confidence in your conclusions. Limit your response to 600 words and 6 images.")
st.divider()

# ----------------------- Importing dataframes -----------------------
nodes = pd.read_csv('Helpers/Dataset/Nodes.csv')
links = pd.read_csv('Helpers/Dataset/Links.csv')
# ---------------------------------------------------------------------

# add a entities
entities = ["Mar de la Vida OJSC", "979893388",
            "Oceanfront Oasis Inc Carriers", "832", "All", "All-entities"]

rc1, rc2, rc3 = st.columns(3)

to_investigate = rc3.selectbox("Please select one entity to investigate:",entities)

st.write("Generating graph for entity:", to_investigate)
# filtering the entities
if to_investigate != "All-entities" or to_investigate != "All":
    c1 = links['source'] == to_investigate
    c2 = links['target'] == to_investigate
    filter_links = links[c1 | c2]

elif to_investigate == "All":
   filter_links = links

elif to_investigate == "All-entities":
    c1 = links['source'].isin(entities)
    c2 = links['target'].isin(entities)
    filter_links = links[c1 | c2]


source = filter_links["source"]
target = filter_links["target"]
weight = filter_links["weight"]
relation = filter_links["type"]

edge_data = zip(source, target, weight, relation)


net = Network(notebook=False,cdn_resources="remote",
              height=str(HEIGHT)+"px", width="100%", bgcolor="#0e1117",
              font_color="white", directed=True)



#net.force_atlas_2based()
# net.hrepulsion()
net.barnes_hut(
    gravity= -80000,
    central_gravity=0.1,
    spring_length=100,
    spring_strength=0.001,
    damping=0.02,
    overlap=0
)
net.set_edge_smooth("dynamic")
#net.toggle_physics()
#net.show_buttons(filter_=['physics'])
#net.inherit_edge_colors(status=True)
net.show_buttons()

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    rel = e[3]

    net.add_node(src, src, title=src, color="#03DAC6", shape='box', value=10)
    net.add_node(dst, dst, title=dst, color="#da03b3", shape='triangle')
    net.add_edge(src, dst, value=w, color="#018786", title=rel)

neighbor_map = net.get_adj_list()

# for node in net.nodes:
#   node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
#   node["value"] = len(neighbor_map[node["id"]])

# Save and read graph as HTML file (on Streamlit Sharing)
try:
   html_path = 'Helpers'
   net.save_graph(f'{html_path}/pyvis_graph.html')
   HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()
# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    net.save_graph(f'{html_path}/pyvis_graph.html')
    HtmlFile = open(f'{html_path}/pyvis_graph.html','r',encoding='utf-8').read()

# Load HTML into HTML component for display on Streamlit
components.html(HtmlFile, height=HEIGHT, width=WIDTH)