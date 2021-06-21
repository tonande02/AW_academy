#! /bin/bash

echo -n "Please enter your age: "
read age

if [ $age -gt 17 ]
    then
        echo "You are legally an adult"
    else
        echo "You are legally not an adult"
fi