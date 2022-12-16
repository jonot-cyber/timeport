#!/usr/bin/env python3

import fire

def timeport(time, from_="UTC", to="UTC"):
    return (time, from_, to)

if __name__ == "__main__":
    fire.Fire(timeport)
