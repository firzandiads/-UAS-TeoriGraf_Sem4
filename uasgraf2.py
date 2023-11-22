#Fauzie, Ikmal, Zandi

#import NetworkX dan Matplotlib
import networkx as nx
import matplotlib.pyplot as plt
#objek arah grafnya
G = nx.DiGraph()

#node/username twitter
G.add_node('Zandi')     
G.add_node('Ikmal')     
G.add_node('Fauzie')    
G.add_node('Aiman')     
G.add_node('Zaki')      
G.add_node('Ihza')      
G.add_node('Najib')     
G.add_node('Shella')    
G.add_node('Azam')      
G.add_node('Fathin')    
G.add_node('Imam')      
G.add_node('Davin')     
G.add_node('Shakti')    
G.add_node('Salma')     

#arah hubungan
G.add_edge('Zandi', 'Salma')
G.add_edge('Zandi', 'Shella')
G.add_edge('Ikmal', 'Davin')
G.add_edge('Fauzie', 'Ikmal')
G.add_edge('Fauzie', 'Shakti')
G.add_edge('Fauzie', 'Imam')
G.add_edge('Aiman', 'Ihza')
G.add_edge('Zaki', 'Davin')
G.add_edge('Zaki', 'Shakti')
G.add_edge('Zaki', 'Najib')
G.add_edge('Ihza', 'Davin')
G.add_edge('Ihza', 'Shakti')
G.add_edge('Ihza', 'Fathin')
G.add_edge('Najib', 'Salma')
G.add_edge('Najib', 'Zaki')
G.add_edge('Shella', 'Zaki')
G.add_edge('Fathin', 'Zaki')
G.add_edge('Imam', 'Shakti')
G.add_edge('Imam', 'Salma')
G.add_edge('Davin', 'Ikmal')
G.add_edge('Davin', 'Zaki')
G.add_edge('Shakti', 'Salma')
G.add_edge('Shakti', 'Imam')
G.add_edge('Salma', 'Shakti')

#menggambar grafnya
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_color='black', arrows=True)
#menampilkan gambarnya
plt.show()