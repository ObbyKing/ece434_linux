Exercise 15

1) Target = app.o
2) Dependency = app.c
3) Command = gcc

-c Compile or assemble the source files, but do not link. The linking stage simply is not done. The Ultimate output is in the form of an object file for each source file.

First run!
Hello, World! Main is executing at 0x400596
This address (0x7fff0c1c22e0) is in our stack frame
This address (0x601048) is in our bss section
This address (0x601040) is in our data section

Cross compiling run!
Hello, World! Main is executing at 0x103d5
This address (0xbe814c54) is in our stack frame
This address (0x21030) is in our bss section
This address (0x21028) is in our data section

I performed part 1, 2 and 3 for the kernel exercises.

I ran into the seg fault issue in part 2 for exploring BB and fixed them accordingly.

I changed the pin numbers in part 3 from the default values to gpioLED = 48 and gpioButton = 117.

With the help of Dr. Yoder I also made the button trigger on IRQF_TRIGGER_RISING and IRQF_TRIGGER_FALLING by or'ing them together in result.

Dr. Yoder verified that the LKM worked correctly.

========================
Professor Yoder's Comments

Looks good.  

I don't see where you compiled a new kernel and got it installed.

Score:  8/10
