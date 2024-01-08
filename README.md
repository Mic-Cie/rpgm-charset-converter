# rpgm-charset-converter
This script is meant to convert the CharSets from RPG Maker 2000/2003 to a format usable in RPG Maker XP.

# Prerequisites

* Python installed
* Pillow package (to install: ***pip3 install pillow***)

# Usage
Example input picture:

![](/img/example.png)

The input picutre is in RPG Maker 2000 format - 288x256px, 256 color, no alpha channel. The CharSet contains 8 characters, each having 16 sprites, 3 per direction.

Using the script:
``` bash
python .\convertRm2KCharsetToXP.py img/example.png
```

8 new images should be generated, in this instance ***example_1.png***, ***example_73.png***, ***example_129.png***, ***example_145.png***, ***example_201.png***, ***example_217.png***, ***example_273.png*** and ***example_345.png***.

example_1.png:

![](/img/example_1.png)

Each resulting image contains only one of the 8 characters. Walking directions are reordered to match XP format and each animation contains 4 frames now. The resulting image is scaled up twice, using nearest neighbour interpolation (no antialiasing). The palette is true color now (PNG-24) with an alpha channel.

By default, the most abundant color gets replaced with transparent pixels. This behavior can be turned off with a flag:
``` bash
python .\convertRm2KCharsetToXP.py img/example.png --no-remove
```

example_1.png in this case:

![](/img/example_1_noremove.png)