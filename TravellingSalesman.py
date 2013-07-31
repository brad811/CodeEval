import sys
import math

locations = []
distances = []
currentMinimum = 100000
minList = []
remaining = []
visited = []
total = 0

# Travel to the current node and recurse until all locations are visited,
# or until the current distance is more than the minimum distance so far
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

# Open the input file
fileName = sys.argv[1]
fileData = open(fileName, 'r').read().split('\n')

# Process each line of the input file, parsing the locations
for line in fileData:
	if line == '':
		continue
	location = line.split('(')[1].replace(')','').replace(' ','').split(',')
	location[0] = float(location[0])
	location[1] = float(location[1])
	locations.append(location)

# Calculate the distances between the list of locations, given in latitudes and longitudes.
# Example input line:
# 1 | CodeEval 1355 Market St, SF (37.7768016, -122.4169151)
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
			
			# Calculate the distance between the two locations
			# The radius of the earth is 6371km
			a = math.sin(latDiff/2) * math.sin(latDiff/2) + math.sin(lonDiff/2) * math.sin(lonDiff/2) * math.cos(lat1) * math.cos(lat2)
			dist.append(6371 * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))
	
	distances.append(dist)

# Start from location 1
visited.append(0)
remaining = range(1, len(locations))

# Visit each location from location 1
for next in remaining:
	travel(remaining[:], visited[:], 0, next, total, distances)

# Print out the locations listed in the best path found
for loc in minList:
	print loc + 1
