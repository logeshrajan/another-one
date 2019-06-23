n = int(input())
numbers = []
for _ in range(n):
    num = input()
    numbers.append(num)
for i in numbers:
    # if i.isalpha() or i.isdecimal():
    #     print(False)
    #     continue;

    if i.isdecimal():
        print(True)
    else:
        print(False)

