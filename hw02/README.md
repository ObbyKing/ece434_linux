I used curses for etch-a-sketch but it should be preinstalled on the bone and you should be able to run in.

My pin definitions are as follows

buttonUp = P9_27
buttonDown = P9_16
buttonLeft = P9_17
buttonRight = P9_18
buttonQuit = P9_22
buttonShake = P9_24

buttonsAndLEDS.py is my python file to map buttons to LEDs.
toggle.py and toggleinC.c are my programs used to toggle GPIO ports.
etch-a-sketch.py is my python file used for etch-a-sketch.

They all work according to the specifications.

Bash and Shell
1) Max Voltage = 3 V, Min Voltage = 80 mV
2) Period = 1 / f = 1 / 4.235 Hz = 0.236 s
3) 0.236 - 0.1 = 0.136 ms
4) They differ because the gpio port cannot toggle as quickly as the value we have passed in.
5) I'm using 18.3% CPU
6) 0.05 period = 0.048 s = 29.4%, 0.02 period = 0.0198 s = 50%, 0.009 = 0.0088 s = 70%, 0.007 = 0.0064 s = 73.3%, 0.004 = 0.0034 s = 83.7%, 0.002 = 0.00198 s = 90.9%, 0.0009 = 0.00087 s = 96%, 0.0007 = 0.00066 s = 96.7%, 0.0003 = 0.00027 s = 98.7%, 0.0001 = 0.000098 s = 99.4% < - This is the fastest I think we can go.
7) The period is not stable at all, there are periods on the oscilloscope that are noticeably larger than others.
8) With lags a little bit and I would assume this is because the BeagleBoard is dedicating all of it's CPU usage to togglegpio.sh
9) Removing comments and unnecessary lines actually did greatly increase stability.
10) The period is not shorter and more unstable
11) The shortest period I can get is 0.0001 s

Python
1) Max Voltage = 3 V, Min Volage = 80 mV
2) Period = 1 / f = 1 / 10.76 Hz = 0.0929 s
3) 0.1 - 0.0929 = 0.0071
4) They differ because the gpio port cannot toggle as quickly as the value we have passed in. Also, the cpu lags a little when handling the processor.
5) I'm using 3.2% CPU
6) 0.05 = 0.048 s = 2.6%, 0.02 = 0.0198 s = 4%, 0.01 = 0.0098 s = 6.6%, 0.005 = 0.0041 s = 8%, 0.0002 = 0.000172 s = 17.2%, 0.0001 = 0.000091 s = 69.2%, 0.00005 = 0.000043 s = 74.1%, 0.000002 = 0.00000194 s = 76.7%, 0.00000002 = 0.0000000194 s = 80%, 0.00000001 = 0.0000000094 s = 74%, This is going very quickly.
7) The period is not stable at all.
8) Vi lags a little
9) I don't have any unnecessary lines and it's extremely fast

C
1) Max Voltage = 3 V, Min Voltage = 80 mV
2) Period =  1 / f = 1 / 9.82 Hz = 0.101 s
3) 0.1 - 0.101 = -0.001
4) They differ according to #4 in previous answers
5) I'm using 2% CPU
6) 10 ms = 9.7 ms = 3.3%, 1 ms = 0.92 ms = 5.5%, 100 us = 99.8 us = 22.4%, 10 us = 9.77 us = 31.6%
7) the period is not stable at all.
8) Vi makes the period less stable
9) I removed my unnecessary lines and it made it slightly more stable.
