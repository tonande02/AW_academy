#! /bin/bash

echo "Hello, there! What is your name?"


if [ -z $1 ]
    then
        echo "Y u no tell me name :("
        exit -1
    else
        echo "Hey, $1! Nice to meet you. Where do you live?"
fi


if [ -z $2 ]
    then
        echo "Y u no tell me location :(("
        exit -1
    else
        echo "Cool, I've never been to $2. What's your favourite colour?"
fi


if [ -z $3 ]
    then
        echo "Y no tell me nothing :'("
        exit -1
    else
        echo "Whaat, my favourite colour is also $3!"
fi

echo "*********"
echo "Nice, $1, $2, and $3. Cheers, thanks, byee!"