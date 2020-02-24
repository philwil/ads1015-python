#!/usr/bin/env python
import time
from ads1015 import ADS1015

#CHANNELS = ['in0/ref', 'in1/ref', 'in2/ref']
CHANNELS = ['in1/ref']


print("""read-georgina.py - read in1/ref input of the ADC

Press Ctrl+C to exit!
""")

ads1015 = ADS1015()
ads1015.set_mode('single')
ads1015.set_programmable_gain(2.048)
ads1015.set_sample_rate(1600)

reference = ads1015.get_reference_voltage()

print("Reference voltage: {:6.3f}v \n".format(reference))

try:
    while True:
        for channel in CHANNELS:
            value = ads1015.get_compensated_voltage(channel=channel, reference_voltage=reference)
            print("{}: {:6.3f}v".format(channel, value))

        print("")
        time.sleep(0.25)

except KeyboardInterrupt:
    pass
