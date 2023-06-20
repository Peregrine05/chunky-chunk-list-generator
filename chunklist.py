import argparse
import json
from math import floor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates a Chunky \"chunkList\" from a pair of input coordinates")
    parser.add_argument("X1", help="X-coordinate of one corner of the selection", type=int)
    parser.add_argument("Z1", help="Z-coordinate of one corner of the selection", type=int)
    parser.add_argument("X2", help="X-coordinate of the opposite corner of the selection", type=int)
    parser.add_argument("Z2", help="Z-coordinate of the opposite corner of the selection", type=int)
    parser.add_argument("-c", "--chunks", help="Use chunk coordinates instead of block coordinates",
                        action="store_true")
    args = parser.parse_args()

    x_min, x_max = sorted((args.X1, args.X2))
    z_min, z_max = sorted((args.Z1, args.Z2))
    use_chunk_coordinates = args.chunks

    if not use_chunk_coordinates:
        x_min = floor(x_min / 16)
        x_max = floor(x_max / 16)
        z_min = floor(z_min / 16)
        z_max = floor(z_max / 16)

    chunk_list = {"chunkList": []}

    for x in range(x_min, x_max + 1):
        for z in range(z_min, z_max + 1):
            chunk_list["chunkList"].append([x, z])

    def write(mode):
        with open("chunkList.json", mode) as file:
            json.dump(chunk_list, file, indent=2)

    try:
        write("x")
    except FileExistsError:
        write("w")
