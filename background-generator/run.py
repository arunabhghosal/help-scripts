#!/usr/bin/python
from PIL import Image, ImageDraw, ImageColor
import random
import sys
import math

def main():
	if len(sys.argv) != 3:
		print "\nUsage: \n$ python run.py <screen_width> <screen_height>\n"
		exit()

	# get the output image resolution as command line arguments
	img_res = (int(sys.argv[1]), int(sys.argv[2]))
	img_format = "JPEG"
	colors = ("#EF5350", "#42A5F5", "#66BB6A", "#FFEE58", "#78909C")

	# set a random color as background
	img = Image.new("RGB", img_res, colors[random.randint(0, 4)])

	# draw vertical stripes on the image
	draw = ImageDraw.Draw(img)
	i = 0
	j = 0
	stripe_width = img_res[0] / 10
	stripe_length = img_res[1]
	for i in range(0, img_res[1], stripe_width):
		draw.rectangle(((i, j), (i + stripe_width, stripe_length)), fill=ImageColor.getrgb(colors[random.randint(0, 4)]));

	# save the image as a jpeg file
	img.save("image_1." + img_format, img_format)

if __name__ == "__main__":
	main()
