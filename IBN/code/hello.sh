#! /bin/bash

echo "Hello World"
new_var=10 
new_var2="String"
myhost=$(hostname)
myhost=`hostname` #alternative schreibweise zu 
echo "new_var hat den Wert $new_var"
echo "\$myhost = $myhost"
echo $(pwd)
echo $(ls -la)

# parameter
$1, $2, $3 
# als ./skriptname 1 2 3 ... fur $1, $2, $3...
echo $1
echo $2 
echo $3