#!bin/bash

echo "Dame el gpio:"
read ngpio

echo $ngpio > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$ngpio/direction

for i in 0 1 2 3 4 5
do

	echo "1" > /sys/class/gpio/gpio$ngpio/value
	sleep 1 
	echo "0" > /sys/class/gpio/gpio$ngpio/value
	sleep 1 #//para ver la velocidad maxima (comentarlos)
done

echo $ngpio > /sys/class/gpio/gpio$ngpio/unexport

exit 0

