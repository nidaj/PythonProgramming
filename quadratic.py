"""
@Author : Nida Jawre
@Date: 2021-06-02
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-02
@Title: Program to find roots of quadratic equation
"""
import math


def calculate_roots(l):
    """
    Description : Function to calculate roots
    :param l: is a list of 3 numbers a,b,c
    :return: root1 and root2 in a list
    """
    roots = []
    delta = (l[1] ** 2) - (4 * l[0] * l[2])
    root1 = (-1 * l[1] + math.sqrt(delta)) / (2 * l[0])
    roots.append(round(root1, 2))
    root2 = (-1 * l[1] - math.sqrt(delta)) / (2 * l[0])
    roots.append(round(root2, 2))
    return roots


def display_roots(root):
    """
    Description: Function to displays calculated roots of quadratic equation
    :param root: list containing 2 calculated roots
    :displays: root1 and root2 values
    """
    print(f"root1 = {root[0]} and root2 = {root[1]}")


def accept_a_b_c():
    """
    Description: Function to accept 2 integers
    returns a list containing values of a,b,c
    """
    list_a_b_c = []
    a = int(input("Enter a: "))
    list_a_b_c.append(a)
    b = int(input("Enter b: "))
    list_a_b_c.append(b)
    b = int(input("Enter b: "))
    list_a_b_c.append(b)
    return list_a_b_c


try:
    root = calculate_roots(accept_a_b_c())
    display_roots(root)
except Exception as e:
    print(e)
