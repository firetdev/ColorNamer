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
        return 255
    return math.sqrt(diff['r'] * diff['r'] + diff['g'] * diff['g'] + diff['b'] * diff['b'])

# kMeans function
def getCentroid(img, x):
    spectrumImg = Image.open(img)
    pixels = spectrumImg.load()
    # Create colors array
    colors = []
    for i in range(0, spectrumImg.size[0]):
        colors.append(Clr(pixels[i, 10][0], pixels[i, 10][1], pixels[i, 10][2]))
    # Assign centroids
    centroidSet = [
        Clr(pixels[x[0], 10][0], pixels[x[0], 10][1], pixels[x[0], 10][2]),
        Clr(pixels[x[1], 10][0], pixels[x[1], 10][1], pixels[x[1], 10][2]),
        Clr(pixels[x[2], 10][0], pixels[x[2], 10][1], pixels[x[2], 10][2]),
        Clr(pixels[x[3], 10][0], pixels[x[3], 10][1], pixels[x[3], 10][2]),
        Clr(pixels[x[4], 10][0], pixels[x[4], 10][1], pixels[x[4], 10][2]),
        Clr(pixels[x[5], 10][0], pixels[x[5], 10][1], pixels[x[5], 10][2]),
        Clr(pixels[x[6], 10][0], pixels[x[6], 10][1], pixels[x[6], 10][2])
    ]
    # Do centroid averaging
    for u in range(0, 100):
        groups = [[], [], [], [], [], [], []]
        prevDist = 10000000
        index = ''
        for i in colors:
            for e in range(0, 7):
                if distance(i, centroidSet[e]) < prevDist:
                    prevDist = distance(i, centroidSet[e])
                    index = e
            groups[index].append(i)
        for i in range(0, 7):
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
            centroidSet[i].r = totals['g'] / (len(groups[i]) + 1)
            centroidSet[i].r = totals['b'] / (len(groups[i]) + 1)
    return centroidSet

# Get centroids
myImage = input('Image: ')
coordsFileName = input('File with coords of 7 colors: ')
coordsFile = open(coordsFileName, 'r')
coords = []
for i in coordsFile:
    coords.append(int(i))
coordsFile.close()
centroids = getCentroid('image.jpg', coords)
output = ''
for i in centroids:
    output += i.toString() + '\n'
outputFile = open('training.txt', 'w')
outputFile.write(output)
outputFile.close()