#!/bin/bash

fileName=$1
sudo mkdir tools
cd tools
while read -r line;do
	git clone $line".git"
done<$path"/"$fileName
