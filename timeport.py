#!/usr/bin/env python3

import fire

# You can't use "from" as an argument because it's a reserved keyword
# To make this work with fire, I had to add the underscore. Thanks
# ChatGPT!
def timeport(time, from_="UTC", to="UTC"):
    return (time, from_, to)

if __name__ == "__main__":
    fire.Fire(timeport)
