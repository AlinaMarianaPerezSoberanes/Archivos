#!/bin/bash

cadena="Hola Mundo"
arreglo=(12 34 7 8 3)

function suma1
{
	let var_sum=0
	for i in 0 1 2 3 4
	do
		let var_sum=var_sum+arreglo[i]
	done
	echo "La suma es: $var_sum"
}

function suma2
{
	let var_sum=0
	for i in ${arreglo[*]}
	do
		let var_sum=var_sum+i
	done
	echo "La suma2 es: $var_sum"
}


function suma3
{
	let var_sum=0
	for (( i=0 ; $i < ${#arreglo[*]} ; i= $i + 1 ))
	do
		let var_sum=var_sum+arreglo[i]
	done
	echo "La suma3 es: $var_sum"
}

echo "Esta es la cadena $cadena"
echo "Esta es el arreglo $arreglo"
echo "Esta es el arreglo $arreglo"
echo "Este es el elemento 1 del arreglo ${arreglo[1]}"
echo "Este son todos los elementos del arreglo ${arreglo[*]}"
echo "Este es el numero de elementos del arreglo ${#arreglo[*]}"

suma1
suma2
suma3
exit 0