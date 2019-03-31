#!/usr/bin/env python

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def setting():
 e=list()
 with open('data.txt') as f:
    lines = f.read().split('\n')
    for l in lines:
      e.append(Convert(l))
 e2=e[0:14]
 nodeL=[i[0] for i in e2]
 nodeR=[i[1] for i in e2]
 vertex=nodeL+nodeR
 vertex=list(set(vertex))
 edge=sorted(e2,key=lambda x: float(x[2]))
 return (vertex,edge)

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = list()
    edges = G["edges"]

    for edge in edges:
        vertice1, vertice2, weight = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree

### Starting 
V,E = setting()
G = {
        'vertices': V,
        'edges': E }

MST=kruskal(G)
sum=0
for m in MST:
 print(m)
 sum=sum+float(m[2])

print("Sum distance of MST: "+str(sum))
