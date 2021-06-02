"""
@Author : Nida Jawre
@Date: 2021-06-02
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-02
@Title: Program to find triplets from an array of numbers which adds up to zero
"""
import math


def calculate_distance(l):
    """
    Description : Function to calculate euclidean distance
    :param l: is a list of 2 numbers
    :return: euclidean distance
    """
    distance = math.sqrt(l[0] ** 2 + l[1] ** 2)
    return distance

def accept_integers():
    """
    Description: Function to accept 2 integers

    """
    list_x_y = []
    x = int(input("Enter x: "))
    list_x_y.append(x)
    y = int(input("Enter y: "))
    list_x_y.append(y)
    return list_x_y


try:
    print(calculate_distance(accept_integers()))
except Exception as e :
    print(e)