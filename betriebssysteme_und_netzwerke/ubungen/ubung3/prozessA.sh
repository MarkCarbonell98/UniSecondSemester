#! /bin/bash

mkfifo myIncrediblePipe
echo $1 > myIncrediblePipe