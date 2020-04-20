#!/bin/bash

while read line; do
	echo "$line"

	python write_exec_files.py $line
	
	chmod +x *

	gfortran -O3 -o vectorq.exe vectorq.f

	gfortran -O3 -o omegainv.exe omegainv.f

	./vectorq.exec

 	./omegainv.exec

done <date_list.txt