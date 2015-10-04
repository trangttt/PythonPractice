from collections import defaultdict
import sys
import re
from datetime import timedelta

_RATIO = 1.609344

def convert_time(s):
    hour, min, sec = [int(t) for t in s.split(':')]
    return timedelta(hours=hour, minutes=min, seconds=sec)

def parse_input(file):
   #reading speed limit
    m = re.search('Speed limit is (?P<speed_limit>[0-9.]+) (?P<unit>(mph|hm/h))', file.readline())
    speed_limit = float(m.group('speed_limit'))
    unit = m.group('unit')
    if unit == 'mph':
        speed_limit *= _RATIO
    # print(speed_limit, unit)

    #reading camera
    camera = []
    while True:
        m = re.search('Speed camera number (?P<number>[0-9]+) is (?P<distance>[0-9]+) metres down the motorway', file.readline())
        if m :
            camera.insert(int(m.group('number')), int(m.group('distance')))
        else: break
    # print(camera)

    #reading log
    cars = defaultdict(list)
    while True:
        s = file.readline()
        if s == '': break
        m = re.search('Vehicle (?P<registration_number>[0-9A-Z ]+) passed camera (?P<cam>[0-9]+) at (?P<time>[0-9:]+).', s)
        if m:
            cars[m.group('registration_number')].append((int(m.group('cam')), convert_time(m.group('time'))))
        else: continue
    # print(cars)

    for car in cars:
        log = cars[car]
        for i in range(0, len(log)-1):
            (c1, t1) = log[i]
            (c2, t2) = log[i+1]
            hour = (t2 - t1).seconds / 3600
            distance = (camera[c2-1] - camera[c1-1])/1000
            print("hour {hour} distance {dist}".format(hour=hour, dist=distance))
            speed = distance/ hour
            print("speed {speed}".format(speed=speed))
            if speed > speed_limit:
                speed -= speed_limit
                if unit == 'mph':
                    speed = speed / _RATIO
                    print('Vehicle {rn} broke the speed limit by {amount:>6.02f} mph.'.format(rn=car, amount=speed))
                else :
                    print('Vehicle {rn} broke the speed limit by {amount:>6.02f} km/h.'.format(rn=car, amount=speed))


if __name__ == "__main__":
    parse_input(open(sys.argv[1]))
