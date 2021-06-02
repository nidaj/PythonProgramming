"""
@Author : Nida Jawre
@Date: 2021-06-02
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-02
@Title: Program to find triplets from an array of numbers which adds up to zero
"""

from array import *


def accept_array():
    """
    Desciption
    Function to accepts inputs from user
    :return:array of numbers
    """
    arr = array('i', [])
    size = int(input("Enter the size of array: "))
    print("Enter the elements of an array: ")
    for i in range(size):
        arr.append(int(input()))
    return arr


def findtriplets(arr):
    """
    Desciption
    Function to finds 3 distinct numbers from the array whose sum equals zero and displays it
    """
    flag = False
    size = len(arr)
    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if arr[i] + arr[j] + arr[k] == 0:
                    flag = True
                    print(f"{arr[i]} {arr[j]} {arr[k]}")
    if not flag:
        print("Such Triplet does not exits")


try:
    arr = accept_array()
    findtriplets(arr)
except Exception as e:
    print(e)
