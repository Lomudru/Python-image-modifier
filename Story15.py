import os
from PIL import Image

def Make_gif(input, output):
    Files = os.listdir(input)
    Files = [Image.open(f"{input}/{file}") for file in sorted(Files)]
    Files[0].save(f'{output}/Image.gif', save_all=True, append_images=Files[1:], optimize=False, duration=1000, loop=0)
print(Make_gif("imgGif","img"))