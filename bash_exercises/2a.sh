#! /bin/bash

echo "Hello, there! What is your name?"
read name

if [ -z $name ]
    then
        echo "Y u no tell me name :("
        exit -1
    else
        echo "Hey, $name! Nice to meet you. Where do you live?"
fi

read location

if [ -z $location ]
    then
        echo "Y u no tell me location :(("
        exit -1
    else
        echo "Cool, I've never been to $location. What's your favourite colour?"
fi

read colour

if [ -z $colour ]
    then
        echo "Y no tell me nothing :'("
        exit -1
    else
        echo "Whaat, my favourite colour is also $colour!"
fi

echo "*********"
echo "Nice, $name, $location, and $colour. Cheers, thanks, byee!"