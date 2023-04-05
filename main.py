"""
usage:
    python main.py --image="RhythmGameSprites.png" --sprites=".sprites"
    python main.py --image="RhythmGameSprites.png" --sprites=".sprites" --output="output"
"""


import argparse
import os

from PIL import Image
from pydantic import parse_file_as

from model import Sprites

parser = argparse.ArgumentParser()
parser.add_argument('--image', help='image resource path')
parser.add_argument('--sprites', help='unity .sprites file path')
parser.add_argument('--output', help='output path', default='output')
args = parser.parse_args()

path_image: str = args.image
path_sprites: str = args.sprites
path_output: str = args.output

sprites = parse_file_as(Sprites, path_sprites)
image = Image.open(path_image)

if not os.path.exists(path_output):
    os.makedirs(path_output)

for sprite in sprites.__root__:
    rect = sprite.Base.m_Rect
    image_width, image_height = image.size

    x = rect.x
    y = image_height - rect.y - rect.height
    width = rect.width
    height = rect.height
    box = (
        x,
        y,
        x + width,
        y + height
    )

    image.crop(box).save(f'{path_output}/{sprite.Base.m_Name}.png')
