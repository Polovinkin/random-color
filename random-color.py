import random
from PIL import Image

r = round(random.random() * 255)
g = round(random.random() * 255)
b = round(random.random() * 255)

colors = (r, g, b)
print(colors)
img = Image.new('RGB', (500, 500), colors)
img.show()