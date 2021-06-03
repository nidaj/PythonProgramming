"""
@Author : Nida Jawre
@Date: 2021-06-03
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-03
@Title: Program to to keep track of wins and losses of gambler
"""
import random


def play(stake, goal):
    """
    Description: keep track of whether the gambler wins or goes broke
    :param stake: integer input from user
    :param goal:  interger input from user
    :return: number of wins and losses
    """
    wins = 0
    loss = 0
    while stake >= 1:
        bet = round(random.random(), 2)
        if bet < 0.5:
            wins += 1
            stake += 10
        else:
            loss += 1
            stake -= 10
        if stake < 1:
            print("Gone Broke by: ")
            return wins, loss
        if stake == goal:
            print("Reached Goal by: ")
            return wins, loss


try:
    # keep running until correct inputs is fed
    while True:
        stake_value = int(input("Enter the stake money: "))
        goal_value = int(input("Enter the goal value: "))
        # validating inputs
        if 1 < stake_value < goal_value:
            outcome = play(stake_value, goal_value)
            print(f"wins = {outcome[0]} and loss = {outcome[1]}")
            exit()
except Exception as e:
    print(e)
