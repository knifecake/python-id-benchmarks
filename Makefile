.PHONY: run
run:
	pytest bench.py \
		--benchmark-group-by=func \
		--benchmark-autosave \
		--benchmark-name=short \
		--benchmark-columns=mean,stddev