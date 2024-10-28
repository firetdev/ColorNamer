import math
from PIL import Image

centroids = []  # Array of centroids (will be put into centroids.txt)

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
    return math.sqrt(diff['r'] * diff['r'] + diff['g'] * diff['g'] + diff['b'] * diff['b'])

# kMeans function
def getCentroid(img, x, names):
    spectrumImg = Image.open(img)
    pixels = spectrumImg.load()
    groups = []
    groupsDefault = []
    # Create colors array
    colors = []
    for i in range(0, spectrumImg.size[0]):
        colors.append(Clr(pixels[i, 10][0], pixels[i, 10][1], pixels[i, 10][2]))
    # Assign centroids
    centroidSet = []
    for i in range(0, len(x)):
        centroidSet.append(Clr(pixels[x[i], 10][0], pixels[x[i], 10][1], pixels[x[i], 10][2]))
        groups.append([])
        groupsDefault.append([])
    # Do centroid averaging
    for u in range(0, 100):
        groups = groupsDefault
        for i in colors:
            prevDist = 10000000
            index = ''
            for e in range(0, len(x)):
                dist = distance(i, centroidSet[e])
                if dist < prevDist:
                    prevDist = dist
                    index = e
            groups[index].append(i)
        for i in range(0, len(x)):
            totals = {
                'r': 0,
                'g': 0,
                'b': 0
            }
            for e in groups[i]:
                totals['r'] += e.r
                totals['g'] += e.g
                totals['b'] += e.b
            centroidSet[i].r = totals['r'] / (len(groups[i]) + 1)
            centroidSet[i].g = totals['g'] / (len(groups[i]) + 1)
            centroidSet[i].b = totals['b'] / (len(groups[i]) + 1)
    finalData = {
        'centroids': centroidSet,
        'names': names
    }
    return finalData

# Get input
myImage = input('Image: ')
coordsFileName = input('File with coords of colors: ')
namesFileName = input('File with color names: ')

# Prepare coordinates and names
coordsFile = open(coordsFileName, 'r')
coords = []
for i in coordsFile:
    coords.append(int(i))
coordsFile.close()
namesFile = open(namesFileName, 'r')
myNames = []
for i in namesFile:
    myNames.append(i)
namesFile.close()

# Get centroids
data = getCentroid('image.jpg', coords, myNames)
centroids = data['centroids']

# Write output
output = ''
for i in range(0, len(centroids)):
    output += centroids[i].toString() + ' ' + data['names'][i]
outputFile = open('training.txt', 'w')
outputFile.write(output)
outputFile.close()