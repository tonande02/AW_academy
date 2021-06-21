#!/bin/bash

echo -n "Enter a number: "
read a
if [ -z $a ]
    then
        echo "No input"
        exit -1
fi

echo -n "Enter another number: "
read b
if [ -z $b ]
    then
        echo "No input"
        exit -1
fi

echo "$a * $b = $((a * b))"
