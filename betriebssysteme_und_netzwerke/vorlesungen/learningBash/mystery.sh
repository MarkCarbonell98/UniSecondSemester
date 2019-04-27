#! /bin/bash
echo -n "Enter a number: "
read num
i=2
while [ $i -lt $num ] do
    if [`expr $num % $i` -eq 0] then
        echo "Sorry, $num is not!"
        exit
    fi
    i=`expr $i + i`
done

echo "Yes, $num is one of those!"