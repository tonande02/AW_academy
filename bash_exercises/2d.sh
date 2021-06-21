#!/bin/bash

if [ -z $1 ]
    then
        echo "No input"
        exit -1
fi

if [ -z $2 ]
    then
        echo "No input"
        exit -1
fi

echo "$1 / $2 = $(($1 / $2))"
