# chunky-chunk-list-generator

## Usage

This script requires that [Python 3](https://www.python.org/) be installed.

Run the script with the command: `python chunklist.py <args>`.

```
usage: chunklist.py [-h] [-c] [-s SCENE] X1 Z1 X2 Z2

Creates a Chunky "chunkList" from a pair of input coordinates

positional arguments:
  X1                    X-coordinate of one corner of the selection
  Z1                    Z-coordinate of one corner of the selection
  X2                    X-coordinate of the opposite corner of the selection
  Z2                    Z-coordinate of the opposite corner of the selection

optional arguments:
  -h, --help            show this help message and exit
  -c, --chunks          Use chunk coordinates instead of block coordinates
  -s SCENE, --scene SCENE
                        Location of the scene description file to which to
                        write the "chunkList"
```

If `--scene` is not specified, then the script will write a "chunkList.json" file to the working directory. Replace the `"chunkList"` section of a Chunky "scene.json" file with the contents of the "chunkList.json" file, without the curly braces.

Delete the "scene.octree2" file, if present, and load the scene in Chunky. Chunky will load the chunks specified in the "scene.json" file.
