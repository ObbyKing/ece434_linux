Bash and Shell
1) Max Voltage = 3 V, Min Voltage = 80 mV
2) Period = 1 / f = 1 / 4.235 Hz = 0.236 s
3) 0.236 - 0.1 = 0.136 ms
4) They differ because the gpio port cannot toggle as quickly as the value we have passed in.
5) I'm using 18.3% CPU
6) 0.05 period = 0.048 = 29.4%, 0.02 period = 50%, 0.009 = 70%, 0.007 = 73.3%, 0.004 = 83.7%, 0.002 = 90.9%, 0.0009 = 96%, 0.0007 = 96.7%, 0.0003 = 98.7%, 0.0001 = 99.4% < - This is the fastest I think we can go.
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
6) 0.05 = 2.6%, 0.02 = 4%, 0.01 = 6.6%, 0.005 = 8%, 0.0002 = 17.2%, 0.0001 = 69.2%, 0.00005 = 74.1%, 0.000002 = 76.7%, 0.00000002 = 80%, 0.00000001 = 74%, This is going very quickly.
7) The period is not stable at all.
8) Vi lags a little
9) I don't have any unnecessary lines and it's extremely fast

C
1) Max Voltage = 3 V, Min Voltage = 80 mV
2) Period =  1 / f = 1 / 9.82 Hz = 0.101 s
3) 0.1 - 0.101 = -0.001
4) They differ according to #4 in previous answers
5) I'm using 2% CPU
6) 10 ms = 3.3%, 1 ms = 5.5%, 100 us = 22.4%, 10 us = 31.6%
7) the period is not stable at all.
8) Vi makes the period less stable
9) I removed my unnecessary lines and it made it slightly more stable.
