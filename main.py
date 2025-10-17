import numpy as np
from skimage import color

mode = "rgb"  # Change to "lab" for Lab color space. RGB for which color is technically closer, Lab for which looks closer.

# Define a set of colors with their RGB values
colors = np.array([
    [255,   0,   0],   # Red
    [255, 165,   0],   # Orange
    [255, 255,   0],   # Yellow
    [  0, 128,   0],   # Green
    [  0,   0, 255],   # Blue
    [ 75,   0, 130],   # Indigo
    [238, 130, 238],   # Violet
    [255, 255, 255],   # White
    [  0,   0,   0],   # Black
    [128, 128, 128],   # Gray
    [150,  75,   0]    # Brown
])

# Names corresponding to the defined colors
color_names = [
    "Red", "Orange", "Yellow", "Green", "Blue", "Indigo",
    "Violet", "White", "Black", "Gray", "Brown"
]

print(f"Mode: {mode}"). # So the user knows which mode is active
user_color = input("Enter a color in the format r,g,b: ")
new_color = np.array([int(x) for x in user_color.split(',')])  #Convert input string to RGB array

# Convert from 0-255 to 0-1 range for processing
colors_rgb = colors / 255.0
new_color_rgb = new_color / 255.0

# Convert to Lab
colors_lab = color.rgb2lab(colors_rgb.reshape(1, -1, 3)).reshape(-1, 3)
new_color_lab = color.rgb2lab(new_color_rgb.reshape(1,1,3)).reshape(3,)

# Calculate distances based on selected mode
if mode == "rgb":
    distances = np.linalg.norm(colors_rgb - new_color_rgb, axis=1)
elif mode == "lab":
    distances = np.linalg.norm(colors_lab - new_color_lab, axis=1)

# Output closest color
closest_index = np.argmin(distances)
print("Closest color:", color_names[closest_index])