#!/bin/sh
temp=`i2cget -y 2 0x48`
temp2=$(($temp*2+32))
echo $temp
echo "temp1 in Farhenheit: " $temp2
temp=`i2cget -y 2 0x49`
temp3=$(($temp*2+32))
echo $temp
echo "temp2 in Farhenheit: " $temp3
