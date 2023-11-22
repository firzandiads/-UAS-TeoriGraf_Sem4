import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('user1')
G.add_node('user2')
G.add_node('user3')

G.add_edge('user1', 'user2')
G.add_edge('user2', 'user3')
G.add_edge('user3', 'user1')

nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_color='black')

plt.show()
