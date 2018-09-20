I started with the temperature sensors. I have one temp sensor tied to ground and one tied to high.
In my script, I read both of the addresses and convert the value to Fahrenheit. This worked correctly.

I then moved onto etch-a-sketch. I got the LED matrix working with the buttons first before the rotary encoders.
The buttons successfully worked and then I moved onto the encoders.

Run the following commands to get the encoders to work properly
config-pin P8_33 qep
config-pin P8_35 qep

config-pin P8_41 qep
config-pin P8_42 qep

I ran etch-a-sketch.py and demoed it to Dr. Yoder. It worked correctly.

I also added a clear button and a quit button to my project.



========================
Professor Yoder's Comments

Looks good.  How are your temp sensors wired?

Score:10/10