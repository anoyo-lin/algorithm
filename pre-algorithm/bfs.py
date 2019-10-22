#!/usr/bin/python3
def bfs(graph_vertice_name):
    from collections import deque
    searched = []
    search_queue = deque()
    search_queue += graph[graph_vertice_name]

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_target(person):
                print ('{0} is the target person'.format(person))
                return True
            else:
                #it must have a list to record the searched vertice, else, it will enter dealock if the graph is cyclic
                searched.append(person)
                search_queue += graph[person]
    return False
def is_target(person):
    import re
    ending_k = re.compile('^.*k#')
    if ending_k.search(person):
        return True
    else:
        return False
