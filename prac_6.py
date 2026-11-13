n = int(input("Enter the numbr of departments or institutes: "))

names = []
for i in range(n):

    name = input ("Enter name of place "+ str(i) + ":")
    names.append(name)

print("\nEnter the distance matrix (in meters).")
print("Enter 0 if there is no direct road between two places")

graph = []
for i in range (n):
    row = []
    for j in range(n):
        d = int (input("Distance form "+ names[i]+ " to " + names[j]))
        row.append(d)
    graph.append(row)

#Show the adjacency matrix
print("\nAdjacency matrix")
for row in graph:
    print(row)


#--- kruskals algorithm ------
#idea sort all the edges by distance, then keep adding the smallest
#edges that doesnot form a cycle

def find(parent ,x):
    #finde leader of the group that x belongs to
    while parent[x] !=x:
        x = parent[x]
    return x

edges = []
for i in range (n):
    for j in range(i+1,n):
        if graph[i][j]!=0:
            edges.append((graph[i][j],i ,j ))
edges.sort()

parent = list(range(n))
mst =[]
total = 0

for dist, u,v in edges:
    root_u = find(parent, u)
    root_v = find(parent ,v)
    if root_u != root_v:
        mst.append((u,v,dist))
        total += dist


#------Show the result ------
print("\n Minimum spanning tree using kruskal's algorithm")
for u, v, d in mst:
    print(names[u] + "----" + names[v] + ":" + str(d) + "m")
print("total distance = ", total ,"m")

if len(mst)<=0:
    print("The graph is fully connected")