find . -type d -wholename '*/original' | while read ori_fdr; do
	find $ori_fdr -type f -exec chmod 440 {} +
done
