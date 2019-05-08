#!/bin/bash

if [ ! -d $1 ]
then 
    echo "input is not directory"
    exit -1
fi
then 
echo "zero"
directory=$(pwd)/
else
    last_character=$(echo $directory | rev | cur -c -1)
    if [$last_character == '/']
    then   
        directory=$(pwd)/$directory
    else   
        directory=$(pwd)/directory/
    fi
fi

echo $directory

read -p "Choose option (crtime, ctime, mtim, atime) : " : time_option #input text

if [ $time_option == 'ctime' -o $time_option == 'mtime' -o $time_option == 'atime']
o -a !
then 
    position=6
fi

if[ $time_option == 'crtime' ]
then 
    echo "this is"
    position=5
fi
echo $position
file=$(ls -p $1 | grep -v \| grep '.*\.jpg\|.*\.png')
cd $directory
for i in $files
do 
    echo $i
    file_path=$(readlink -f $i) #returns abs path to file
    echo $file_path

    time=$(sudo debugfs -R "stat $file_path" /dev/nvme0n1p2 | grep $time_option |cut -d " " $position - | rev cut -d " " 1,3- --output-delimiter="." | rev | tr -d '.' | cut -c 1-3,4- --output-delimiter='-' | rev | cut -c 1-4, 5- --output-delimiter="-" | rev | awk -F '-' '{print $3, $2, $1}' OFS=- $file)

    echo $time
    if [ ! -d $time ]
    then
        echo "creating folder $directory$time"
    fi
done
