from random import choice
from pyknow import *

# muasya samuel kyama
# p15/42924/2017

class Temperature(Fact):
    """Info about the temperature of the room."""
    pass


class AdjustFanSpeed(KnowledgeEngine):
    # rule fired when temp is low
    @Rule(Temperature(temperature=10))
    def reduce_fan_speed(self):
        print("The temperature is 10\n")
        print("reduce fan speed. It's too cold in here")

    # rule fired when temp is at a medium level
    @Rule(Temperature(temperature=20))
    def maintain_speed(self):
        print("The temperature is 20\n")
        print("Keep the speed there. The temperature is okay\n")

    # rule fired when temp is too high
    @Rule(Temperature(temperature=25))
    def increase_speed(self):
        print("The temperature is 25\n")
        print("Be increase fan speed because temperature is high", )

fan = AdjustFanSpeed()
fan.reset()
# choose the value of temperature at random
print("enter the value of temperature: either 10 or 20 or 25")
try:
    temp_val = int(input())
    fan.declare(Temperature(temperature=temp_val))
    fan.run()
except:
    print("you must input an integer")


# this program runs on the pyknow expert system shell
# the goal was to create a simple self adjust fan that either increases or reduces its speed based on the temperature
# of the room
# how to run :
# on the console, use:  python3 fan_adjust.py