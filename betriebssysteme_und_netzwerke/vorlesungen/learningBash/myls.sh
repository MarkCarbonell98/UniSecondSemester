#! /bin/bash
actual_dir=$(pwd)
$1 
cd $1
ls -la
cd $actual_dir