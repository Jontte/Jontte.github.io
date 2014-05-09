#!/bin/bash

for FOO in */*jpg */*png; do 
	echo $FOO;
	mkdir -p thumbs/`dirname $FOO`
	convert $FOO -resize '100x100' thumbs/$FOO
done
