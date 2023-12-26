# Video-Killer
Using ffmpeg to i don't even know

i bet this is one of the most fragile scripts on the planet so just.. copy my exact environment and workflow to not break it
I recommend h264 video

options:
  -h, --help            show this help message and exit
  -i ITERATIONS, --iterations ITERATIONS   How many times the video will be ran through the script
  -b BITRATE, --bitrate BITRATE            Bitrate (Default is lossless i think? check ffmpeg docs)
  -s SCALE, --scale SCALE                  Video resolution, example: 512:-1 (512px width and keep aspect ratio)
  -o OUTPUT, --output OUTPUT               Output folders for videos (Default is file name)
(i absolutely just copied this from argparse)
