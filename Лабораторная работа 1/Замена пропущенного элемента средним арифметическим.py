numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
num1 = numbers[0:4]
num2 = numbers[5:20]
numall = num1 + num2
averaga = sum(numall)/len(numbers)
numbers[4] = averaga
print("Измененный список:", numbers)
