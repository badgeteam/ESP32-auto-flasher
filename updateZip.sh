#!/usr/bin/env bash

set -e

cd firmware/locfd

for type in sl n f; do
	# create with maximum compression to a temporary file.
	zip -r -9 ../locfd-$type.zip.$$ . -x .ds_store

	# always do an atomic move.
	mv ../locfd-$type.zip.$$ ../locfd-$type.zip
done
