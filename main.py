"""
usage:
    python main.py --image="RhythmGameSprites.png" --sprites=".sprites"
    python main.py --image="RhythmGameSprites.png" --sprites=".sprites" --output="output"
"""

import argparse
import os

from PIL import Image
from pydantic import parse_file_as

from model import Sprites, Asset

parser = argparse.ArgumentParser()
parser.add_argument('--image', help='image resource path')
parser.add_argument('--sprites', help='unity .sprites file path', default=None)
parser.add_argument('--asset', help='unity .asset file path', default=None)
parser.add_argument('--output', help='output path', default='output')
args = parser.parse_args()

path_image: str = args.image
path_sprites: str = args.sprites
path_asset: str = args.asset
path_output: str = args.output

image = Image.open(path_image)
image_width, image_height = image.size

if not os.path.exists(path_output):
    os.makedirs(path_output)

if path_sprites is not None:

    sprites = parse_file_as(Sprites, path_sprites)

    for sprite in sprites.__root__:
        rect = sprite.Base.m_Rect

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
        print(f'{width}x{height} {sprite.Base.m_Name}')

elif path_asset is not None:

    assets = parse_file_as(Asset, path_asset)

    for asset in assets.Base.mSprites:
        x = asset.x
        y = asset.y
        width = asset.width
        height = asset.height
        box = (
            x,
            y,
            x + width,
            y + height
        )

        image.crop(box).save(f'{path_output}/{asset.name}.png')
        print(f'{width}x{height} {asset.name}')

else:
    print('no sprites or asset file')
