names = ["Admin Block", "Library", "Computer Dept", "Entc Dept", "Mechanical Dept", "Civil Dept", "Management Institute"]

n = len(names)

#------Adjacency matrix (distance in meters)
#---- 0 Means there is no direct road between the two places
graph = [
    #Adm lib cs elc mec civ mgt
    [0, 100, 200, 0, 0, 0, 150 ], #Admin block
    [100, 0, 120, 180, 0, 0, 0 ], #library
    [200, 120, 0, 90, 250, 0, 0], #Computer Dept
    [0, 180, 90,  0, 140,210, 0], #Entc Dept
    [0,  0, 250, 140, 0, 10, 300], #mech dept
    [0,  0,  0, 210,  100, 0, 170], #civil dept
    [150, 0, 0,  0, 300, 170,  0], #management dept
]

#-----Prim's algorithm-------
# Idea : Start form one node. keep adding the smallest edge that
# connects the tree to a node that is not yet in the tree

visited = [False] *n
visited[0] = True       #Start from admin block  
mst = []
total = 0

for _ in range(n - 1):
    best = 999999
    best_u = -1
    best_v = -1

    for u in range (n):
        if visited[u]:
            for v in range(n):
                if not visited[v] and graph[u][v]!=0:
                                if graph[u][v] < best:       #Smaller than best
                                    best = graph[u][v]
                                    best_u = u
                                    best_v = v
            
    visited[best_v] = True         #Add the new node
    mst.append((best_u, best_v, best))
    total += best

# --------- Show the result ---------
print("Adjacency Matrix : ")
for row in graph:
    print(row)

print("\n Minimum Spanning Tree using Prim's algorithm: ")
for u, v, d in mst:
    print(names[u] + "----" + names[v] + " : " + str(d) + "m")
print("Total distance = ", total, "m")


