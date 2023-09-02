even_count = 0
odd_count = 0
numbers = input("Enter a series of numbers : ")
number_list = numbers.split()
for num in number_list:
    num = int(num)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)