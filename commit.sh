#!/bin/sh
read -p "Enter commit message :" msg;
git add .
echo "Added all files"
git commit -m $msg
echo "Commit successful!"
