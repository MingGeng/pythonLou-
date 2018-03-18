#!/bin/sh

times=540000
i=0

while [ "$i" -le "$times" ]
do
    i=$(($i+1))
    echo $i
    echo $i > echo.echo
    sleep 0.5s
    ls ../
done



