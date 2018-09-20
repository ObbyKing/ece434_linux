#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr_gpio0;
    volatile void *gpio_addr_gpio1;
    volatile void *gpio_addr_gpio2;
    volatile void *gpio_addr_gpio3;
    volatile unsigned int *gpio_oe_addr_gpio0;
    volatile unsigned int *gpio_datain_addr_gpio0;
    volatile unsigned int *gpio_oe_addr_gpio1;
    volatile unsigned int *gpio_datain_addr_gpio1;
    volatile unsigned int *gpio_oe_addr_gpio2;
    volatile unsigned int *gpio_setdataout_addr_gpio2;
    volatile unsigned int *gpio_cleardataout_addr_gpio2;
    volatile unsigned int *gpio_oe_addr_gpio3;
    volatile unsigned int *gpio_setdataout_addr_gpio3;
    volatile unsigned int *gpio_cleardataout_addr_gpio3;
    unsigned int reg;

    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    // Begin mapping
    printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, GPIO0_SIZE);
    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);
    printf("Mapping %X - %X (size: %X)\n", GPIO2_START_ADDR, GPIO2_END_ADDR, GPIO2_SIZE);
    printf("Mapping %X - %X (size: %X)\n", GPIO3_START_ADDR, GPIO3_END_ADDR, GPIO3_SIZE);

    // Map corresponding address
    gpio_addr_gpio0 = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
    gpio_addr_gpio1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio_addr_gpio2 = mmap(0, GPIO2_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO2_START_ADDR);
    gpio_addr_gpio3 = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);

    // Map all of the datain, setdata, and cleardata ports
    gpio_oe_addr_gpio0     	 = gpio_addr_gpio0 + GPIO_OE;
    gpio_datain_addr_gpio0 	 = gpio_addr_gpio0 + GPIO_DATAIN;
    gpio_oe_addr_gpio1           = gpio_addr_gpio1 + GPIO_OE;
    gpio_datain_addr_gpio1	 = gpio_addr_gpio1 + GPIO_DATAIN;
    gpio_oe_addr_gpio2           = gpio_addr_gpio2 + GPIO_OE;
    gpio_setdataout_addr_gpio2   = gpio_addr_gpio2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_gpio2 = gpio_addr_gpio2 + GPIO_CLEARDATAOUT;
    gpio_oe_addr_gpio3           = gpio_addr_gpio3 + GPIO_OE;
    gpio_setdataout_addr_gpio3   = gpio_addr_gpio3 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_gpio3 = gpio_addr_gpio3 + GPIO_CLEARDATAOUT;

    if(gpio_addr_gpio0 == MAP_FAILED | gpio_addr_gpio1 == MAP_FAILED | gpio_addr_gpio2 == MAP_FAILED | gpio_addr_gpio3 == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO0 mapped to %p\n", gpio_addr_gpio0);
    printf("GPIO0 OE mapped to %p\n", gpio_oe_addr_gpio0);
    printf("GPIO0 DATAIN mapped to %p\n", gpio_datain_addr_gpio0);
    printf("GPIO1 mapped to %p\n", gpio_addr_gpio1);
    printf("GPIO1 OE mapped to %p\n", gpio_oe_addr_gpio1);
    printf("GPIO1 DATAIN mapped to %p\n", gpio_datain_addr_gpio1);
    printf("GPIO2 mapped to %p\n", gpio_addr_gpio2);
    printf("GPIO2 OE mapped to %p\n", gpio_oe_addr_gpio2);
    printf("GPIO2 SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_gpio2);
    printf("GPIO2 CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_gpio2);
    printf("GPIO3 mapped to %p\n", gpio_addr_gpio3);
    printf("GPIO3 OE mapped to %p\n", gpio_oe_addr_gpio3);
    printf("GPIO3 SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_gpio3);
    printf("GPIO3 CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_gpio3);

    // Set GPIO30 to be an input pin
    reg = *gpio_oe_addr_gpio0;
    printf("GPIO0 configuration: %X\n", reg);
    reg &= GPIO_30;       // Set GPIO30 bit to 1
    *gpio_oe_addr_gpio0 = reg;
    printf("GPIO0 configuration: %X\n", reg);
    // Set GPIO48 to be an input pin
    reg = *gpio_oe_addr_gpio1;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= GPIO_48;       // Set GPIO48 bit to 1
    *gpio_oe_addr_gpio1 = reg;
    printf("GPIO1 configuration: %X\n", reg);
    // Set GPIO88 to be an output pin
    reg = *gpio_oe_addr_gpio2;
    printf("GPIO2 configuration: %X\n", reg);
    reg &= ~GPIO_88;       // Set GPIO88 bit to 0
    *gpio_oe_addr_gpio2 = reg;
    printf("GPIO2 configuration: %X\n", reg);
    // Set GPIO117 to be an output pin
    reg = *gpio_oe_addr_gpio3;
    printf("GPIO3 configuration: %X\n", reg);
    reg &= ~GPIO_117;       // Set GPIO117 bit to 0
    *gpio_oe_addr_gpio3 = reg;
    printf("GPIO3 configuration: %X\n", reg);

    printf("Start reading buttons\n");
    while(keepgoing) {
        // Read button inputs and turn on corresponding LEDs
        if(GPIO_30 & *gpio_datain_addr_gpio0){
	  *gpio_setdataout_addr_gpio2 = GPIO_88;
          usleep(2500);
        }
	else{
	  *gpio_cleardataout_addr_gpio2 = GPIO_88;
          usleep(2500);
	}
        if(GPIO_48 & *gpio_datain_addr_gpio1){
          *gpio_setdataout_addr_gpio3 = GPIO_117;
          usleep(2500);
        }
        else{
          *gpio_cleardataout_addr_gpio3 = GPIO_117;
          usleep(2500);
	}
    }

    // Unmap memory
    munmap((void *)gpio_addr_gpio0, GPIO0_SIZE);
    munmap((void *)gpio_addr_gpio1, GPIO1_SIZE);
    munmap((void *)gpio_addr_gpio2, GPIO2_SIZE);
    munmap((void *)gpio_addr_gpio3, GPIO3_SIZE);
    close(fd);
    return 0;
}
