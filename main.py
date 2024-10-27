from PIL import Image

centroids = {}

class Clr:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

def getCentroid(img, x, y, w, h):
    centroid = Clr(0, 0, 0)
    colors = []
    spectrumImg = Image.open(img)
    pixels = spectrumImg.load()
    # Create colors array
    for i in range(x, x + w):
        for e in range (y, y + h):
            colors.append(Clr(pixels[i, e][0], pixels[i, e][1], pixels[i, e][2]))
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
        centroid.r = total['r'] / len(colors)
        centroid.g = total['g'] / len(colors)
        centroid.b = total['b'] / len(colors)
    return centroid

# Get centroids
centroids['red'] = getCentroid('image.jpg', 0, 0, 50, 306)

