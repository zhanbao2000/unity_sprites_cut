## Tools for Cutting Unity Sprites

### Requirements

 - python 3.8 or later
 - pydantic~=1.10.7
 - Pillow~=9.5.0

```Bash
pip install pydantic Pillow
```

### Usage

```bash
python main.py --image="RhythmGameSprites.png" --sprites=".sprites"
python main.py --image="RhythmGameSprites.png" --sprites=".sprites" --output="output"
```

### Demo

#### image

![`RhythmGameSprites.png`](./assets/RhythmGameSprites.png)

#### sprites

[`.sprites`](./assets/.sprites)

#### output

![`output.png`](./assets/output.png)
