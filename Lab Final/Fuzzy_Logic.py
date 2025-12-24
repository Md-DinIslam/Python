import math
import heapq
from collections import deque

def fuzzify_temperature(temperature):
        cold = triangular(temperature, 0, 0, 20)
        warm = triangular(temperature, 15, 25, 35)
        hot = triangular(temperature, 25, 40, 40)
        return cold, warm, hot

def fuzzy(temperature):
        cold, warm, hot = fuzzy_temperature(temperature)
        speed = cold * 30 + warm * 60 + hot * 90
        total = cold + warm + hot
        if total != 0:
                speed /= total
        return speed

def solve():
       temperature = 28
       fan_speed = fuzzy(temperature)

       print("Speed: ", fan_speed)


if __name__ == '__main__':
        solve()
