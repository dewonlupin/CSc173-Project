import pandas as pd


class Graphs:
    def __int__(self):
        node_file = 'Helpers/Dataset/Nodes.csv'
        link_file = 'Helpers/Dataset/Links.csv'
        self.nodes = pd.read_csv(node_file)
        self.links = pd.read_csv(link_file)

    def create(self, to_investigate):