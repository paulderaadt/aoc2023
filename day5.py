from utils.filereaders import Flatreader
from enum import Enum


class Maps(Enum):
    seedsoil = 'soil-to-fertilizer'
    soilfertilizer = "fertilizer-to-water"
    waterlight = "water-to-light"
    lighttemp = "light-to-temperature"
    temphumidity = "temperature-to-humidity"
    humiditylocation = "humidity-to-location"


rawdata = Flatreader("inputs/day5a.txt").parse()

rawdata = rawdata.split("\n\n")

seeds = [int(seed) for seed in rawdata[0].split(" ")[1:]]
raw_maps = rawdata[1:]


maps = {map.value: None for map in Maps}


def parse_map(map):
    """
    Parse listed input to list of ranges
    source target length
    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4
    :param map: str
    :return:
    """
    header = map.split("\n")[0].split(" ")[0]
    print(header)
    map = map.split("\n")[1:]
    ranges = []
    for line in map:
        line = line.split(" ")
        source, target, length = [int(item) for item in line]
        ranges.append(range(target, length))
    return ranges

[parse_map(map) for map in raw_maps[1:]]