#! /usr/bin/env python3

import datetime
try:  # a non-standard package is used
	from astral import moon
except ModuleNotFoundError:
	exit("\033[1mPackage astral required.\033[0m\nInstall it with 'pip install astral' and try again.")

phase = moon.phase()
lunation = datetime.timedelta(days = (29 - phase) if (phase != 0) else 0, hours = 12, minutes = 44, seconds = 2.8016)
moon = datetime.date.today() + lunation

print("Next new moon: " + moon.strftime("%d %b"))