#! /bin/bash

while read line; 
do
    echo $line | rev;
done < myIncrediblePipe

