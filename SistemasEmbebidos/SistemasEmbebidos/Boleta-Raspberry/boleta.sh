#!/bin/bash

#digitos
cero=(1 1 1 1 1 1 0)
uno=(0 1 1 0 0 0 0)
dos=(1 1 0 1 1 0 1)
tres=(1 1 1 1 0 0 1)
cuatro=(0 1 1 0 0 1 1)
cinco=(1 0 1 1 0 1 1)
seis=(1 0 1 1 1 1 1)
siete=(1 1 1 0 0 0 0)
ocho=(1 1 1 1 1 1 1)
nueve=(1 1 1 0 0 1 1)
#arreglo pines
pines=(17 18 27 22 23 24 25)
#numero boleta
boleta=(2 0 1 5 6 3 0 3 8 0)

for i in 0 1 2 3 4 5 6 7 8 9
do
	#echo $i
	echo ${boleta[$i]}
	case ${boleta[$i]} in
		0) for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${cero[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${cero[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		1)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${uno[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${uno[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		2)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${dos[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${dos[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		3)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${tres[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${tres[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		4)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${cuatro[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${cuatro[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		5)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${cinco[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${cinco[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		6)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${seis[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${seis[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		7)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${siete[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${siete[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		8)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${ocho[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${ocho[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		9)for n in 0 1 2 3 4 5 6
		   do echo "Pin no. ${pines[$n]} y digito ${nueve[$n]}"
			   echo "${pines[$n]}" > /sys/class/gpio/export
			   echo "out" > /sys/class/gpio/gpio${pines[$n]}/direction
				#salida de digitos
				echo "${nueve[$n]}" > /sys/class/gpio/gpio${pines[$n]}/value
		   done;;
		*) echo "No incluido";;
	esac
	sleep 3
done

#desactivar los puertos
for d in 0 1 2 3 4 5 6
do
	echo "${pines[$d]}" > /sys/class/gpio/unexport
done
