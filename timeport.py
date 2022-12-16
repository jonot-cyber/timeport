#!/usr/bin/env python3

import fire

from timezone_list import timezones

def convert_time(time):
    """Converts and formats a 24 hour time"""
    output = ""
    am = True
    while time > 12:
        time -= 12
        am = not am
    output += str(int(time))
    time -= int(time)
    match time:
        case 0.5:
            output += ":30"
        case 0.25:
            output += ":15"
        case 0.75:
            output += ":45"
        case 0:
            output += ":00"
    output += " am" if am else " pm"
    return output

# Since from is a reserved keyword, I can't use it
def timeport(time: str, from_="UTC", to="UTC"):
    time_num = 0
    time = time.lower()
    if time.endswith("pm"):
        time_num = int(time[:time.find("pm")]) + 12
    elif time.endswith("am"):
        time_num = int(time[:time.find("am")])
    else:
        time_num = int(time)
    result = time_num - timezones[from_] + timezones[to]
    return convert_time(result)

if __name__ == "__main__":
    fire.Fire(timeport)
