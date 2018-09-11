#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#include <libsoc_gpio.h>
#include <libsoc_debug.h>

//Blinks an LED attached to P9_12
#define GPIO_OUTPUT	60

int main(void) {
	gpio *gpio_output; // Create gpio pointer
	libsoc_set_debug(1); // Enable debug output
	// Request gpio
	gpio_output = libsoc_gpio_request(GPIO_OUTPUT, LS_SHARED);

	// Set direction to OUTPUT
	libsoc_gpio_set_direction(gpio_output, OUTPUT);

	libsoc_set_debug(0);

	int i;
	for(i = 0; i < 1000000; i++){
		libsoc_gpio_set_level(gpio_output, HIGH);
		usleep(5);
		libsoc_gpio_set_level(gpio_output, LOW);
		usleep(5);
	}

	if (gpio_output){
		// Free gpio request memory
		libsoc_gpio_free(gpio_output);
	}

	return EXIT_SUCCESS;
}
