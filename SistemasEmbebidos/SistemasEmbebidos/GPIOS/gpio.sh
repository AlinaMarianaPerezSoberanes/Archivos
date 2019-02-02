#!bin/bash

echo "17" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio17/direction

while [1]
do

	echo "1" > /sys/class/gpio/gpio17/value
#	sleep 5 
	echo "0" > /sys/class/gpio/gpio17/value
#	sleep 5 //para ver la velocidad maxima (comentarlos)
done

echo "17" > /sys/class/gpio/gpio17/unexport

exit 0

