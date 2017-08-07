#!/usr/bin/env bash

find /home/sdal/projects/ -mindepth 1 -maxdepth 1 -type d | while read proj_fdr
do
	echo $proj_fdr
	stat -c "%G" $proj_fdr
	chgrp -R $(stat -c "%G" $proj_fdr) $proj_fdr
done
