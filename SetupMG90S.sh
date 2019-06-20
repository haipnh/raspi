#!/bin/bash

# This script setup hardware PWM and initialize parameters
# Expected frequency of PWM = (19.2 * 10^6) / (PWMC * PWMR)
# If we want a 50Hz PWM, PWMC=384 and PWMR=1000

# NOTE: MG90S or any actuator need a response time to move mechanical parts. 
# You need to read datasheet carefully and pause after each control command. 
# At 4.8V, MG90S need 0.1s to move 60 degrees.

# RUNNING SETUP AT BOOT
# Save this file as /home/pi/SetupMG90S.sh
# Open rc.local by executing command: 
# $ sudo nano /etc/rc.local
# Add "sudo bash /home/pi/SetupMG90S.sh" above "exit 0" line
# Then reboot the Raspberry Pi

# This script was created on 20th Jun 2019 by haipnh.

# Set HW-PWM mode for GPIO12
gpio mode 26 pwm 
# Set MS PWM mode
gpio pwm-ms
# Set PWMC = 384 
gpio pwmc 384
# Set PWMR = 1000
gpio pwmr 1000

gpio pwm 26 75



# Example commands to rotate the MG90S 180 degree.

# for i in {25..125}
# do
#    gpio pwm 26 $i
#    sleep 0.1
# done

# gpio pwm 26 75
