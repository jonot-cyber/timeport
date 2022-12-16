#!/usr/bin/env python3

import fire

from timezone_list import timezones

# You can't use "from" as an argument because it's a reserved keyword
# To make this work with fire, I had to add the underscore. Thanks
# ChatGPT!
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
    am = True
    while result > 12:
        result -= 12
        am = not am
    return f"{result} {'am' if am else 'pm'}"

if __name__ == "__main__":
    fire.Fire(timeport)
