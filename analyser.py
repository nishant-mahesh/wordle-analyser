import networkx as nx

G = nx.DiGraph()

G.add_node("hello")

word_file = open("words.txt", "r")
word_list = word_file.readlines()
word_list = [line.rstrip() for line in word_list]

word_masks = set()
for i in range(32):
    cur_mask = format(i, "05b")
    for word in word_list:
        masked_word = ""
        for bit in range(5):
            if(cur_mask[bit] == '0'):
                masked_word += '_'
            else:
                masked_word += word[bit]
        word_masks.add(masked_word)

print(len(word_masks))

G.add_nodes_from(word_masks)

for node in G.nodes:
    for i in range(5):
        if(node[i] != '_'):
            from_node = ""
            if(i == 0):
                from_node = '_' + node[1:]
            elif(i == 4):
                from_node = node[:4] + '_'
            else:
                from_node = node[:i] + '_' + node[i + 1:]
        G.add_edge(from_node, node)

print(len(G.nodes))

i = 0
for edge in G.edges:
    i  += 1
    print(edge)
    if(i == 1000):
        break
    
# len(word_masks) is 27023; total number of masks iterated through  will be 32 * 2315 = 74000 approx.


        
    

