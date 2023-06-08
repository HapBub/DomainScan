#!/bin/bash


File=$1

cat $File | while read line

Domain=http://$line

do dirb $Domain

done


