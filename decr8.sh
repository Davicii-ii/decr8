#!/bin/sh
# get audio from soundcloud

filename='/home/decr8/decr8/links.txt'

while :; read line; do
    # reading each line
    scdl -l $line -f -c --path="/home/decr8/music"
    shuf $filename -o $filename
done < $filename
#for i in  {1..10}
#do
#    scdl -l $links
#    echo "Current # $i"
#done    
