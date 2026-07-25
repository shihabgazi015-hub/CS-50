import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    'Gemini_Generated_Image_jemg98jemg98jemg.gif', save_all=True, append_images=images[1:], duration=500, loop=0
)