#!/bin/bash

year=$1
base=$(pwd)

# For some unknown reason, january, february and march seem not to be available

for month in abril mayo junio julio agosto septiembre octubre noviembre diciembre
do
	for table in 501 502 503 504 505 507 509 510 512 520 551 552 553 554 556 557
	do
		echo curl ftp://ftp2.sat.gob.mx/aduanas/$year/Balanza_publica/$month/t$table.zip -O >> $base/download_$year.sh
		echo aws s3 cp t$table.zip s3://aduanas/$year/Balanza_publica/$month/ >> $base/download_$year.sh
		echo rm t$table.zip >> $base/download_$year.sh
	done
done