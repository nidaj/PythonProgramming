"""
@Author : Nida Jawre
@Date: 2021-06-02
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-02
@Title: Program to calculate windchills
"""

import math


def calculate_windchills(v, t):
    """
    Description: Function to calculate the windchills
    :param v: speed of wind in kilometers/hour
    :param t: air temperature in degrees celsius
    :return: windchill value ie wci
    """
    wci = 13.12 + 0.6215 * t - 11.37 * math.pow(v, 0.16) + 0.3965 * t * math.pow(v, 0.16)
    return int(round(wci, 0))


try:
    while True:
        v = float(input("Input wind speed in kilometers/hour: "))
        t = float(input('Input air temperature in degrees Celsius: '))
        if 120 >= v >= 3 and t < 50:
            print("The wind chill index is", calculate_windchills(v, t))
            break
        else:
            print("Enter values range as 120 >= v >= 3 and t > 50")
except Exception as e:
    print(e)
