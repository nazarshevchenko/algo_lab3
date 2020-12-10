  
class Node:
    
    def __init__(self, name):
        self.name = name
        self.length = {}

    def make_connection(self, to, length):
        self.length[to] = length
        to.length[self] = length

    def get_length(self, to=float("inf")):
        if to == float("inf"):
            print(self.length)
        
        elif type(to) == int():
            print(self.length[to])


class Dijkstra:
    def __init__(self, start):
        self.start_node = start
        self.way = {start: 0}
    
    def new_node(self, node):
        self.way[node] = float("inf")
    
    def start(self):
        current_node = self.start_node
        self.way_to(current_node)
        return self.way
        


    def way_to(self, current_node):
        for node in current_node.length.items():
            current = node[0]
            weight = node[1] + self.way[current_node]

            if self.way[current] > weight:
                self.way[current] = weight
                self.way_to(current)
                
            
        



# Write info from file to data
f = open('/Users/macbookpro/algo_lab3/algo_lab3/gamsrv.in', 'r').read().split("\n")

data = []
for i in f:
    data.append(i.split())


N = int(data[0][0])
M = int(data[0][1])

# all clients
client = data[1]


# Create nodes && get nodes wich able to be Server
nodes = []
routes = []
for i in range(N):
    nodes.append(Node(i))
    if str(i + 1) not in client:
        routes.append(str(i + 1))


# make conections
for i in range(M):
    info = data[i + 2]
    first_node = int(info[0])  - 1
    second_node = int(info[1]) - 1
    length = int(info[2])
    
    nodes[first_node].make_connection(nodes[second_node], length)


max_delay = float("inf")
for server in routes:
    p = Dijkstra(nodes[int(server) - 1])
    for node in nodes:
        if node != nodes[int(server) - 1]:
            p.new_node(node)
    result = p.start()

    info = []
    for way in client:
        info.append(result[nodes[int(way) - 1]])
    
    if sum(info) < max_delay:
        max_delay = sum(info)
        best = info


f = open("gamsrv.out", "w").write(str(max(best)))
