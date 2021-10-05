#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program is the positive number adder


def main():
    # This program adds all positive numbers together
    # input
    amount_of_numbers = input("How many numbers are you going to add: ")

    try:
        total = 0
        amount_of_numbers = int(amount_of_numbers)

        for num in range(amount_of_numbers):
            # second input
            number_input = input("Enter a number to add: ")
            # process
            number_input = int(number_input)
            if number_input < 0:
                continue
            total += number_input

        # output
        print("Sum of just the positive numbers is {0}".format(total))
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
