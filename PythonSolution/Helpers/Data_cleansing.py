"""
File is used to enhance the data quality used inside the main program that is Introduction.py.
Only used for data cleansing purpose
Need to run only once
"""
import json
import pandas as pd


PATH = 'Helpers/Dataset/MC1.json'


# open dataset
with open(PATH, 'r', encoding='utf-8') as f:
    data = f.read()

# loading json data
json_data = json.loads(data)

# creating nodes dataframe
nodes = pd.DataFrame(json_data['nodes'])
# creating links dataframe
links = pd.DataFrame(json_data['links'])


# deleting "dataset" from nodes as it has no significance
nodes = nodes.drop('dataset', axis=1)
# deleting "dataset" from link as it has no significance
links = links.drop('dataset', axis=1)

# converting all columns of node_df to strings
node_columns = nodes.columns
for columns in node_columns:
    nodes[columns] = nodes[columns].astype(str)

# converting selected columns to string in link dataframe or,
# we can convert all columns into string to ease the comparison and plotting
links_columns = list(links.columns)
links_columns.remove("weight")
for columns in links_columns:
    links[columns] = links[columns].astype(str)

# replacing nan value of nodes["country"] with "Unknown"
nodes["country"] = nodes["country"].replace("nan", "Unknown")
# replacing None value of nodes["type"] with "Uncategorized"
nodes["type"] = nodes["type"].replace("nan", "Uncategorized")

# creating two more columns in links
# 1. target_country: country of target node
# 2. source_country: country of source node
# 1. target_country
links[]

# ----------------------- saving to .csv -----------------------
# saving nodes dataframe to csv
nodes.to_csv("Helpers/Dataset/Nodes.csv", index=False)
# saving links dataframe to csv
links.to_csv("Helpers/Dataset/Links.csv", index=False)
# --------------------------------------------------------------
