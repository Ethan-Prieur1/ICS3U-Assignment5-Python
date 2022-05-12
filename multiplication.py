#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that goes through the 0-9 multiplication chart


def main():
    # This is the main program
    counter = 0
    counter2 = 0

    # Output
    print("")
    for counter in range(10):
        for counter2 in range(10):
            answer = counter * counter2
            print("{0} x {1} = {2}".format(counter, counter2, answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
