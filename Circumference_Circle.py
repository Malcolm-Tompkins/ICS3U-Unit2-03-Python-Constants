#!/usr/bin/env/ python3

# Created by Malcolm Tompkins
# Created on April 28, 2021
# Calculates the circumference of user input dimensions


import constants


def main():
    # Function that calculates circumference
    radius = int(input("Input the radius of the circle (cm):"))
# User Input
    circumference = constants.TAU * radius
# Process
    print("The circumference is: {} cm".format(circumference))


if __name__ == "__main__":
    main()
