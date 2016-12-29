#!/usr/bin/python
import os
import sys

known_exts = [".mp3", ".m4a", ".wma"]

def main():
	if len(sys.argv) != 2:
		print "Usage `python run.py <path/to/directory>`"
		exit()
	path = sys.argv[1]
	files = os.listdir(path)
	seq = 0
	os.chdir(path)
	files.sort()
	for file in files:
		if os.path.splitext(file)[1] in known_exts:
			if seq < 10:
				seq_str = "0" + str(seq)
			else:
				seq_str = str(seq)
			new_filename = seq_str + " - " + file
			os.rename(file, new_filename)
			print "Renamed " + file + " to " + new_filename + "\n"
			seq += 1

if __name__ == "__main__" :
	main()
