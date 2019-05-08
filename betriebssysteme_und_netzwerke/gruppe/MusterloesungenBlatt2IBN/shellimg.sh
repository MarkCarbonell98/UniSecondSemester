#! /bin/bash

echo "Enter directory:"
read directory

if [ ! -d "$directory" ]
then
  echo "Directory doesnt exist!"
  exit -1
fi

for i in $directory/*
do
  if [[ "$i" == *.png ]] || [[ "$i" == *.jpg ]] || [[ "$i" == *.jpeg ]]
  then
    date=$(date -r "$i" +%Y-%m)
    if [ ! -d "$directory/$date" ]
    then
      mkdir $directory/$date
    fi
    mv $i $directory/$date
  fi
done
