import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('name')
parser.add_argument('-i', '--iterations', type=int,default=8)
parser.add_argument('-b', '--bitrate')
parser.add_argument('-crf', '--crf')
parser.add_argument('-l', '--length', type=int, default=10)
parser.add_argument('-s', '--scale')
parser.add_argument('-ts', '--tmixscale', type=float, default=1)
parser.add_argument('-o', '--output')
parser.add_argument('-m', '--mode', type=int, default=0)

args = parser.parse_args()


file = args.name.split(".")
folder = args.output or file[0]

print(file)
os.system(f"mkdir {file[0]}")

def iter(name_in, name_out):
    command = f"ffmpeg -hide_banner -y -i {name_in} "

    if args.bitrate:
        command += f"-b:v {args.bitrate} "

    if args.crf:
        command += f"-crf {args.crf} "

    command += f"-vf \""

    if args.scale:
        command += f"scale=\"{args.scale}\","

    #command += "format=gbrp,tmix=frames=19:weights='-1 -2 -3 -4 -5 -6 -7 -8 -9 91 -9 -8 -7 -6 -5 -4 -3 -2 -1'[v];[v]format=yuv420p\" " 
    command += "format=gbrp,tmix"

    match args.mode:
        case 0:
            command += f"=frames={args.length}:weights='"
            nums = range(1, args.length)
            for i in nums:
                command += f"-{i} "

            command += f"{sum(nums) + 1}':scale={1/args.length if args.tmixscale == 0.0 else args.tmixscale}"
        case 1:
            command += "=frames=2:weights='-1 2':scale=1"

    command += "[v];[v]format=yuv420p\" "

    command += f"{folder}/{name_out}"

    print(command)

    os.system(command)
    #os.system(f"ffmpeg -i {name_in} -b:v {args.bitrate} -vf \"format=gbrp,tmix=frames=19:weights='-1 -2 -3 -4 -5 -6 -7 -8 -9 91 -9 -8 -7 -6 -5 -4 -3 -2 -1'[v];[v]format=yuv420p\" {name_out}")


new_name = "1" + "." + file[-1]
iter(".".join(file), new_name)
args.scale = None
if args.iterations > 1:
    for i in range(2, args.iterations + 1):
        old_name = new_name
        new_name = str(i) + "." + file[-1]
        # os.system(f"ffmpeg -i {old_name} -vf \"format=gbrp,tmix=frames=19:weights='-1 -2 -3 -4 -5 -6 -7 -8 -9 91 -9 -8 -7 -6 -5 -4 -3 -2 -1'[v];[v]format=yuv420p\" ./{file[0]}/{new_name}")
        iter(f"{folder}/{old_name}", new_name)
