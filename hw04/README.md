See the Pictures/MemoryMapping.jpg to see my memory mapping for the GPIO ports and RAM

My GPIO ports are as follows:

Button0 : P9_11, GPIO0_30, GPIO30
Button1 : P9_15, GPIO1_16, GPIO48
Led0 : P8_28, GPIO2_24, GPIO88
Led1 : P9_25, GPIO3_21, GPIO117

My toggling program can be seein in gpioToggle.c. I got rid of some comments to improve the stability of the period.

The lowest I could get was 168.57us with a frequency of 6.156kHz. This is about twice as fast as the previous assignment. Memory Mapping allows for much faster writing to registers but it is much more tedioous to do.
I really enjoyed doing the memory mapping stuff after learning how it was done.

Check the pictures folder to see my screenshots for the LCD problems. I had a few difficulties at first getting text displayed on Boris but I think it worked out well!

In order to flip the images, I changed the rotation in on.sh

In order to make annotated_boris.png, I used the convert command in ImageMagick.

The command was as follows: convert boris.png -background Khaki label: 'Boris the Dog' -size 1000x160 -gravity Center -append annotated_boris.png

I attempted to get pygame working in class but there was tab indentation errors with the sample code given.
