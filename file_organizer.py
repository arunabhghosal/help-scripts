#!/usr/bin/python
import os
import re
prog_lang = [ "java" , "c" , "cpp" , "py" , "html" , "css" , "rb" , "sh" , "pl" ]
home = os.environ['HOME']+"/test"
os.chdir(home)
files = os.listdir(home)
length = len(files)
for p in prog_lang : 
	
	pattern = re.compile("."+p+"$")
	
	for f in files :
		iter = pattern.findall(f)
		if len(iter) !=0 :
			if p in files :
				os.rename(home+"/"+f,home+"/"+p+"/"+f)
			else :
				os.mkdir(home+"/"+p)
				files.append(p)
				os.rename(home+"/"+f,home+"/"+p+"/"+f)
