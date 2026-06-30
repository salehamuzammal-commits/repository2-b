def calculate_average(numbers):
    total = 0

    for i in range(len(numbers) + 1):   # Bug 1: Goes out of bounds
        total += numbers[i]

    average = total / len(number)       # Bug 2: Wrong variable name
    return average


nums = [10, 20, 30, 40]

print("Average is:", calculate_average(nums))
