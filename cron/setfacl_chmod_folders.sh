#!/usr/bin/env bash

find /home/sdal/projects/ -mindepth 1 -maxdepth 1 -type d | while read proj_fdr
do
	echo $proj_fdr
	chmod -Rv g+s $proj_fdr
	setfacl -d -m g::rwx $proj_fdr
	setfacl -d -m o::rx $proj_fdr
	getfacl $proj_fdr
done
