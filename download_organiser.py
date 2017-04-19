#!/usr/bin/python
import os
import re
file_type = [ "zip" , "pdf" ,"docx" ]


download = os.environ['HOME']+"/Downloads"
os.chdir(download)


files = os.listdir(download)
length = len(files)

if os.path.exists(download+"/"+"folder") == False :
	os.mkdir(download+"/"+"folder")


for f in files :
	if os.path.isdir(f) == True and f != "folder" :
		if f in file_type == False :
			os.rename(download+"/"+f,download+"/"+"folder"+"/"+f)

for t in file_type :
	pattern = re.compile("."+t+"$")
	for f in files :
		iter = pattern.findall(f)
		if len(iter) !=0 :
			if t in files :
				os.rename(download+"/"+f,download+"/"+t+"/"+f)
			else :
				os.mkdir(download+"/"+t)
				files.append(t)
				os.rename(download+"/"+f,download+"/"+t+"/"+f)
