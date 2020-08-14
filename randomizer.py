#! usr/bin.env python
import random
import os

def print_list(numbers_list):
    for number in numbers_list:
        print(number)


def randomizer(numbers_required):
    i = 0
    numbers = []
    while i < numbers_required:
        n = random.randint(1, 500)
        numbers.append(n)
        i = i + 1
    return numbers


random_numbers = randomizer(10)
random_sorted_numbers = sorted(random_numbers)
print_list(random_sorted_numbers)
input("[+] Press ENTER to close...>>")