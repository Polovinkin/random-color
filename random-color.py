import random
from PIL import Image

colors_list = random.sample(range(1,255), 3)
colors = tuple(colors_list)
print(colors)

img = Image.new('RGB', (500, 500), colors)
img.show()