#!/bin/sh

times=540000000
i=0
list=[2,5,10,15,30,600]
while [ "$i" -le "$times" ]
do
    i=$(($i+1))
    echo $i
    echo $i >> echo.echo
    sleep 10s
    ls ../
done



