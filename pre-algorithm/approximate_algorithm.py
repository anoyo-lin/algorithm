#!/usr/bin/python3
stations = {}
stations['kone'] =  set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

print (stations)


for station, state_for_station in stations.items():
    print (station, state_for_station)


state_needed = set(['id', 'nv', 'ut', 'wa', 'id', 'mt', 'or', 'nv', 'ca', 'nv', 'ut', 'ca', 'az'])
final_stations = list()

while state_needed:
    best_station = None
    # pay attention to the condition change, it needs to clear the state_covered status when a loop finished
    state_covered = set()
    for station, state_for_station in stations.items():
        now_covered = state_for_station&state_needed
        if len(now_covered) > len(state_covered):
            best_station = station
            state_covered = now_covered

    final_stations.append(best_station)
    state_needed -= state_covered

print (final_stations)
