#!/bin/bash
echo "Hola mundo"
echo "La suma de 4+3 es: $[4+3]"
echo "La suma de 4+3 es: $((4+3))" #Otra forma de sumar, el $ indica la oprecion
#declarar variables sin espacios
var1=4
var2=8
echo "var1= $var1"
echo "var2= $var2"

suma=$var1+$var2 #sin corchetes se concatenan las cadenas, siempre son cadenas
echo "La suma es: $suma" #Como cadena

let suma=$var1+$var2 #en enteros se usa let
echo "La suma con let es: $suma" #Como int

suma=$[var1+var2] #en enteros con corchetes
echo "La suma con corchetes es: $suma" #Como int

suma=$((var1+var2)) #en enteros con corchetes
echo "La suma con parentesis es: $suma" #Como int