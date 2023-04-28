#!/bin/bash

ssh ubuntu@control.brandsonroad.com
# please comment the below line if mongo connection not created
echo 'mongodump --forceTableScan --db led --gzip --archive=mongoBackup_`date +"%Y-%m-%d.gz"`'
ll