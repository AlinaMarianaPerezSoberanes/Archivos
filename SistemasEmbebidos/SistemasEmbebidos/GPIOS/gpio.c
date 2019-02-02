#include<stdio.h>
#include<unistd.h>
#include<wiringPi.h.>

int main()
{
	wiringPiSetup();
	pinMode(0. OUTPUT);
	while(1)
	{
		digitalWrite(0, HIGH);
//		sleep(5);
		digitalWrite(0, LOW);
//		sleep(5);
	}
	return 0;
}

/*ejecutar con -lwiringPi*/

