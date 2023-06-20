# chunky-chunk-list-generator

## Usage

This script requires that [Python 3](https://www.python.org/) be installed.

Run the script with the command: `python chunklist.py <args>`.

```
usage: chunklist.py [-h] [-c] X1 Z1 X2 Z2

Creates a Chunky "chunkList" from a pair of input coordinates

positional arguments:
  X1            X-coordinate of one corner of the selection
  Z1            Z-coordinate of one corner of the selection
  X2            X-coordinate of the opposite corner of the selection
  Z2            Z-coordinate of the opposite corner of the selection

optional arguments:
  -h, --help    show this help message and exit
  -c, --chunks  Use chunk coordinates instead of block coordinates
```

If successful, the script will write a "chunkList.json" file to the working directory. Replace the `"chunkList"` section of a Chunky "scene.json" file with the contents of the "chunkList.json" file. Delete the "scene.octree2" file, if present. Load the scene in Chunky and Chunky will load the chunks specified in the "scene.json" file.
