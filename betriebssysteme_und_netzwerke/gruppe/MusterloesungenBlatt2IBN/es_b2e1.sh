
#first of all we need to define the interpreter
#Example Solution Erik Koynov
#!/bin/bash

if [ ! -d $1 ]
then 
	echo input is not a directory
	exit -1
fi
directory=$1
position=0

# default option
if [ -z $directory ]
then
echo zero
directory=$(pwd)/
else
	# check format of path
	last_character=$( echo $directory | rev | cut -c -1)
	if [ $last_character == '/' ]
	then 
		directory=$(pwd)/$directory
	else
		directory=$(pwd)/$directory/
	fi

	
fi
echo $directory

read -p "Choose option (crtime, ctime, mtime, atime) :" time_option # to input with friendly text --> read -p
# choose time option
if [  $time_option == 'ctime'  -o  $time_option == 'mtime'  -o  $time_option == 'atime'  ] # logical operators -o -a ! 
then
	position=6
fi

if [ $time_option == 'crtime' ]
then
	echo this is
	position=5
fi
echo $position
# put backslash before the .png because . actually means 1 character
# .* means any number of characters
files=$(ls -p $1 |grep -v /| grep '.*\.jpg\|.*\.png') # never put space between the variable name and the = sign

# no need to cast to an array the interpreter automatically sprits the strings by ' '
for i in $files
do	
	echo $i
	echo file_path is $directory$i
	# to store the output of a probram into a variable $()

	# debugfs needs absolute path
	time=$(sudo debugfs -R "stat $directory$i" /dev/mapper/mint--vg-root | grep $time_option | cut -d " " -f $position- | rev | cut -d " " -f 1,3- --output-delimiter="." | rev | tr -d '.' | cut -c 1-3,4- --output-delimiter='-'|rev | cut -c 1-4,5- --output-delimiter='-'|rev | awk -F '-' '{print $3, $2, $1}' OFS=- $file) # use awk to rearrange the output columns 
	echo $time
	# check if dir exists
	if [ ! -d $time ]
	then
		# make the folder
		mkdir $directory$time
		echo creating folder $directory$time
	fi
	
	
	# copy the file into the destination folder
	cp $directory$i $time
	
done	
	

