import math
import re
from PIL import Image

centroidsArray = []  # Array of centroids (will be put into centroids.txt)

# Color class
class Clr:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue
    def toString(self):
        return str(int(self.r)) + ', ' + str(int(self.g)) + ', ' + str(int(self.b))

# Distance from a centroid
def distance(color, center):
    diff = {
        'r': center.r - color.r,
        'g': center.g - color.g,
        'b': center.b - color.b
    }
    dist = math.sqrt(diff['r'] * diff['r'] + diff['g'] * diff['g'] + diff['b'] * diff['b'])
    if dist == 0:
        return 2048
    else:
        return math.sqrt(diff['r'] * diff['r'] + diff['g'] * diff['g'] + diff['b'] * diff['b'])

# kMeans function
def getCentroid(data):
    text1 = re.sub(r'[A-Za-z]+', '', data)
    text2 = re.sub(r'\d{1,3},\s*\d{1,3},\s*\d{1,3}', '', data)
    groups = []
    groupsDefault = []
    # Get names
    text2 = text2.splitlines()
    names = []
    for i in text2:
        names.append(i)
    # Make colors array
    colors = []
    if True:  # Indent, so that i, e, and u will not carry into next block
        i = 0
        while i < 255:
            e = 0
            while e < 255:
                u = 0
                while u < 255:
                    colors.append(Clr(i, e, u))
                    u += 5
                e += 5
            i += 5
    # Make centroids array
    centroids = []
    rgbValues = text1.splitlines()
    for i in rgbValues:
        match = re.match(r'(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', i)
        if match:
            numbers = match.groups()
            centroids.append(Clr(int(numbers[0]), int(numbers[1]), int(numbers[2])))
            groups.append([])
            groupsDefault.append([])
    oldCentroids = []
    # Do averaging
    for u in range(0, 20):
        oldCentroids = centroids
        groups = groupsDefault
        for i in colors:
            prevDist = 10000000
            index = ''
            for e in range(0, len(centroids)):
                dist = distance(i, centroids[e])
                if dist < prevDist:
                    prevDist = dist
                    index = e
            groups[index].append(i)
        for i in range(0, len(centroids)):
            totals = {
                'r': 0,
                'g': 0,
                'b': 0
            }
            for e in groups[i]:
                totals['r'] += e.r
                totals['g'] += e.g
                totals['b'] += e.b
            centroids[i].r = totals['r'] / (len(groups[i]) + 1)
            centroids[i].g = totals['g'] / (len(groups[i]) + 1)
            centroids[i].b = totals['b'] / (len(groups[i]) + 1)
    finalData = {
        'centroids': centroids,
        'names': names
    }
    return finalData

# Read data
trainingData = ''
with open('trainingData.txt', 'r') as dataFile:
    trainingData = dataFile.read()

# Get centroids
centroidData = getCentroid(trainingData)
centroidsArray = centroidData['centroids']

# Write output
output = ''
for i in range(0, len(centroidsArray)):
    output += centroidsArray[i].toString() + ' ' + centroidData['names'][i] + '\n'
outputFile = open('training.txt', 'w')
outputFile.write(output)
outputFile.close()