#!/usr/bin/env bash

find /home/sdal/projects -type d -wholename '*/original' | while read ori_fdr; do
	echo $ori_fdr
	find $ori_fdr -type f
	find $ori_fdr -type f -exec chmod 440 {} +
done
