#! /bin/bash

if [ -d "$1" ] && { [ $# < 2 ]; }; then
    echo "Directory exists";
    echo $1;
    ls --full-time $1; 
    exit 0;
fi
echo "The directory does not exists"