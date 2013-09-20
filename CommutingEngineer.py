import sys
import math

locations = []
distances = []
currentMinimum = 100000
minList = []
remaining = []
visited = []
total = 0

def travel(remaining, visited, previous, current, total, distances):
	global currentMinimum, minList
	total += distances[previous][current]
	
	if total >= currentMinimum:
		return
	
	remaining.remove(current)
	visited.append(current)
	
	if len(remaining) == 0:
		currentMinimum = total
		minList = visited
		return
	
	for next in remaining:
		travel(remaining[:], visited[:], current, next, total, distances)

fileName = sys.argv[1]
fileData = open(fileName, 'r').read().split('\n')

for line in fileData:
	if line == '':
		continue
	location = line.split('(')[1].replace(')','').replace(' ','').split(',')
	location[0] = float(location[0])
	location[1] = float(location[1])
	locations.append(location)

for start in locations:
	dist = []
	for end in locations:
		if(end == start):
			dist.append(0)
		else:
			latDiff = math.radians(end[0] - start[0])
			lonDiff = math.radians(end[1] - start[1])
			lat1 = math.radians(end[0])
			lat2 = math.radians(start[0])
			
			a = math.sin(latDiff/2) * math.sin(latDiff/2) + math.sin(lonDiff/2) * math.sin(lonDiff/2) * math.cos(lat1) * math.cos(lat2)
			dist.append(6371 * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))
	
	distances.append(dist)

visited.append(0)
remaining = range(1, len(locations))

for next in remaining:
	travel(remaining[:], visited[:], 0, next, total, distances)

for loc in minList:
	print loc + 1
