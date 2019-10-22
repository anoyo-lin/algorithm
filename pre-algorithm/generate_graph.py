#!/usr/bin/python3
#hashmap
graph = {}
graph['gene'] = [ 'neil', 'frank', 'qian']
graph['neil'] = ['maple', 'kevin']
graph['frank'] = ['clark', 'gerry']
graph['qian'] = ['kevin']
graph['kevin'] = []
graph['maple'] = []
graph['clark'] = []
graph['gerry'] = []

from collections import deque
import re
def person_is_seller(person):
    ending_with_k = re.compile('.*k$')
    if ending_with_k.search(person):
        return True
    else:
        return False

def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print (person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
print (bfs('gene'))
