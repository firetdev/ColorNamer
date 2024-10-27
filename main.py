from PIL import Image

centroids = {}  # Dictionary of centroids (will be put into centroids.txt)

# Color class
class Clr:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

# kMeans function
def getCentroid(img, x, w):
    centroid = Clr(0, 0, 0)
    spectrumImg = Image.open(img)
    pixels = spectrumImg.load()
    # Create colors array
    colors = []
    for i in range(x, x + w):
        colors.append(Clr(pixels[i, 10][0], pixels[i, 10][1], pixels[i, 10][2]))
    # Do centroid averaging
    for u in range(0, 100):
        total = {
            'r': 0,
            'g': 0,
            'b': 0
        }
        for i in colors:
            total['r'] += i.r
            total['g'] += i.g
            total['b'] += i.b
        centroid.r = round(total['r'] / len(colors))
        centroid.g = round(total['g'] / len(colors))
        centroid.b = round(total['b'] / len(colors))
    return centroid

# Get centroids
centroids['red'] = getCentroid('image.jpg', 0, 74)
centroids['orange'] = getCentroid('image.jpg', 74, 53)
centroids['yellow'] = getCentroid('image.jpg', 127, 84)
centroids['green'] = getCentroid('image.jpg', 211, 145)
centroids['blue'] = getCentroid('image.jpg', 356, 173)
centroids['purple'] = getCentroid('image.jpg', 530, 54)
centroids['pink'] = getCentroid('image.jpg', 584, 43)
