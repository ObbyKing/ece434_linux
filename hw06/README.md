I added project ideas to the sheet last week and put my name down on projects that I would be interested in learning.

1. Where does Julia Cartwright work?
National instruments

2. What is PREEMT_RT? Hint: Google it.
Real-Time Patch. It allows for soft real-time performances using the Linux kernel.

3. What is mixed criticality?
A mixing of tasks. Some may be time critical while others are not time critical.

4. How can drivers misbehave?
The driver stacks are shared between the RT tasks and the Non-RT Tasks.

5. What is Δ in Figure 1?
The time between an event being raised and an event being serviced. 

6. What is Cyclictest[2]?
Take a timestamp, sleep for a fixed duration, takes a time stamp when a thread wakes up. Take the difference between the timestamps and the sleep duration and that is the delta.

7. What is plotted in Figure 2?
The delta values for preempt and preempt_rt

8. What is dispatch latency? Scheduling latency?
Dispatch latency: Amount of time it takes for the hardware to fire to the interrupt dispatch for the relevent thread to actually wake up. Scheduling latency: Amount of time it takes for the high priority scheduler to send data to the CPU.

9. What is mainline?
A model. A model with interrupts explicitly disabled.

10. What is keeping the External event in Figure 3 from starting?
A low priority interrupt. In the figure it's the non critical IRQ.

11. Why can the External event in Figure 4 start sooner?
Because the IRQ's are now running in a thread, they can be preempted. So, if a high pripority IRQ thread fires, that can be scheduled immediately.

This lecture is extremely techincal and a little difficult to follow. I sort of understand what is going on, but perhaps the lecture on Thursday will help reinforce the material.

========================
Professor Yoder's Comments

Score:  10/10

Try searching "linux mainline kernel"