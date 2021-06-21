#! /bin/bash
echo "Hey there, what's your name?"
read name
if [ -z "$name" ]
    then
        echo "You did not answer!"
        exit -1
    else
        echo "welcome $name, how are you doing?"
fi
read how
if [ -z "$how" ]
    then
        echo "You did not answer!"
        exit -1
    else
        echo "Thanks $name, I am also doing $how!"
fi
read
echo "*******************"
echo "I am just a simple script, that's all I have to say, bye!"