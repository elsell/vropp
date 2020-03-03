import pychromecast
import sys
import os
from time import sleep
try:
    import readline
except ImportError:
    import pyreadline as readline

hLine = "=" * 80
header = ""
about = "The One-Stop Shop for Annoying Your Fellow Google Cast Users"
with open("header", "rb") as headFile:
    header =  headFile.read().decode("UTF-16")

print(hLine)
[print(line.center(80)) for line in header.splitlines()]
print(about.center(80))
print(hLine)

print("Performing Discovery for Cast Devices...")
l = (pychromecast.get_chromecasts())
print("Discovered {} Cast Devices:".format(len(l)))
print()

def completer(text, state):
    options = [cmd for cmd in [cc.device.friendly_name for cc in l] if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while(True):
    print("TARGETS\n" + "-"*80)
    [print(n) for n in sorted([cc.device.friendly_name for cc in l])]
    print("_"*80,"\nEND TARGETS\n")
    target = input("selectTarget> ")
    print("Connecting to {}...".format(target))
    try:
        cast = next(cc for cc in l if cc.device.friendly_name == target)
        cast.wait()
        print("Connected.")
        num = input("attackRange> ")
        print("Attacking for range {}...".format(num))
        for i in range(0, int(num)):
            i = i % 10
            i = i / 10
            cast.set_volume(i)
            sleep(.4)
        print("Attack Complete.\n\n")
        input("[ENTER] To Continue...")

    except Exception as e:
        print("[ fail ] Could not connect to {}. Exception: {}".format(target,str(e)))
