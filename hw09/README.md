I started the homework and had issues getting my LED to flash. I had to switch kernels in order to get the LED to flash. I'm now using 4.14.62-ti-r70 kernel.

See tek00000 image to see the waveform for 2.6 Blinking an LED. The period was 80.11 and the frequency was 12.48 MHz. This was the fastest I could get it. There is a lot of jitter on the port.

See tek00001 image to see the waveform for 5.3 PWM Generator. I made the waveform symmetric but I could not make the frequency 50 MHz. I'm not sure how to calculate the STD. There is jitter on the edges of the waveform.

See tek00002 image to see the waveform for 5.4 Controlling the PWM Frequency. The frequency I could get was 326.8kHz. This frequency is limited by how quickly you switch channels in the code.

See tek00003 image to see the waveform for 5.5 Loop Unrolling for Better Performance. The speedup goes from 362 kHz to 1.68 MHz.

See tek00004 image to see the waveform for 5.9 Read an Input at Regular Intervals. The code transfers the input to the output extremely quickly!


========================
Professor Yoder's Comments

In part 5.3 I don't think it jitter, it's ringing.
5.9, how quickly is it responding?

Score:  10/10
