distance = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distance.keys():
        print(f"{name} is {distance[name]} AU away from Earth")
    print()
    distance_in_meters(distance)


def distance_in_meters(dist):
    for distances in dist.values():
        print(f"{distances} AU is {convert(distances)} meters")
    

def convert(au):
    return au * 149597870700




main()