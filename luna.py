#! /usr/bin/env python3

import datetime
try:  # a non-standard package is used
	import astral
except ImportException:
	exit("\033[1;91mPackage astral required.\n\033[0;91mInstall it with 'pip install astral' and try again.\033[0m")  # ANSI escape sequences fuck yeah!

phase = astral.Location(("","",0,0,"UTC",0)).moon_phase()
lunation = datetime.timedelta(days = (29 - phase) if (phase != 0) else 0, hours = 12, minutes = 44, seconds = 2.8016)
moon = datetime.date.today() + lunation

while (astral.Location(("","",0,0,"UTC",0)).moon_phase(moon) != 1):
	moon += datetime.timedelta(days = 1)

print("Next new moon: " + moon.strftime("%d %b"))