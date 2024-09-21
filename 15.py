def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

print(find_maximum([]))


# output yang diharapkan: tidak ada hasil
# tanpa mengganti parameter fungsi