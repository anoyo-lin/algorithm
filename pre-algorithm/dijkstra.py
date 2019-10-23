#!/usr/bin/python3
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a']  = 3
graph['b']['fin'] = 5
graph['fin'] = {}

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

processed = []

print (graph)

node = find_lowest_cost_node(costs)
while node is not None:
    neighbors = graph['node']
    old_cost = costs[node]
    for n in neighbors.keys():
        new_cost = old_cost + graph[node][n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_node = None
    for n in costs:
        if n not in processed:
            if costs[n] < lowest:
                lowest_cost = costs[n]
                lowest_node = n
    if lowest == infinity:
        return None
    else:
        return lowest_node
