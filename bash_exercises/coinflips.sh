# didn't finish this, am trying to use the modulo to see if nr is
# odd (tails) or even (heads), but am doing smt wrong

#! /bin/bash


# COIN_FLIPS = 5 in local environment

for ((i = 1; i <= $COIN_FLIPS; i++)); 
    do
    
        if [ $($RANDOM % 2) == 1 ]
            then
                echo "Tails"
            else
                echo "Heads"
        fi
    done