#!/bin/bash
function op_suma {
    echo "Dame el número 1"
    read n1
    echo "Dame el número 2"
    read n2
    let suma=n1+n2 #sin corchetes se concatenan las cadenas, siempre son cadenas
    echo "La suma de $n1 + $n2 es: $suma" #Como cadena
}

function op_resta {
    let resta=$1-$2 #sin corchetes se concatenan las cadenas, siempre son cadenas
    echo "La resta de $1 - $2 es: $resta" #Como cadena
}

function op_multi {
    let multi=$1*$2 #sin corchetes se concatenan las cadenas, siempre son cadenas
    echo "La multiplicacion de $1 * $2 es: $multi" #Como cadena
}

function op_div {
    echo "Dame el número 1"
    read n1
    echo "Dame el número 2"
    read n2
    let div=n1/n2 #sin corchetes se concatenan las cadenas, siempre son cadenas
    echo "La div de $n1 / $n2 es: $div" #Como cadena
}


echo "1.Operacio  de suma"
echo "2.Operacio  de resta"
echo "3.Operacio  de multiplicacion"
echo "4.Operacio  de division"
read opcion
case $opcion in
    1)
        op_suma
    ;;
    2)
        echo "Dame el número 1"
        read n1
        echo "Dame el número 2"
        read n2
        op_resta $n1 $n2
    ;;
    3)
        echo "Dame el número 1"
        read n1
        echo "Dame el número 2"
        read n2
        op_multi $n1 $n2
    ;;
    4)
        op_div 
    ;;
    *)
        echo "Opcion incorrecta"
    ;;
esac