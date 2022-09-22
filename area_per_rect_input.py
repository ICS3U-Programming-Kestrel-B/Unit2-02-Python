#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 22, 2022
# This program calculates the area and perimeter
# of a rectangle with user input


import math


def main():
    # input
    print("This program calculates the area")
    print("and perimeter of a rectangle.")
    print("")
    length = int(input("Enter the length in mm: "))
    width = int(input("Enter the width in mm: "))

    # process
    area = length * width
    perimeter = 2 * length + 2 * width

    # output
    print("")
    print("Area = {}mm^2".format(area))
    print("Perimeter = {}mm".format(perimeter))


if __name__ == "__main__":
    main()
