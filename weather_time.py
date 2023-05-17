#!/usr/bin/env python3

import datetime

time_local = datetime.datetime.now()

current_hour = int(time_local.strftime("%H"))

salutations = (
    "Доброе утро!",
    "Добрый день!",
    "Добрый вечер!",
    "Доброй ночи!",
)

g_m, g_d, g_e, g_n = salutations

# clear, cloudy, rain, storm
day_icons = ("\ue30d", "\ue30c", "\ue30b", "\ue30e")
night_icons = (
    "\ue32b",
    "\ue37e",
    "\ue326",
    "\ue329",
)
rain, storm, sun_storm = ("\ue314", "\ue315", "\ue30e")


def salute():
    if current_hour in range(4, 12):
        salu = g_m
    elif current_hour in range(12, 18):
        salu = g_d
    elif current_hour in range(18, 22):
        salu = g_e
    else:
        salu = g_n

    return salu


def choose_icons():
    icons = night_icons
    if current_hour in range(4, 19):
        icons = day_icons

    return icons
