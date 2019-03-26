#연습문제 1
list1 = ['Life', 'is', 'too', 'short']
print(" ".join(list1))
print("\n")

#연습문제 2
print("shirt")
print("\n")

#연습문제 3
n = 1
while n < 5:
    print("*"*n)
    n += 1
print('\n')

#연습문제 4
str1 = 'mutzangesazachurum'
n = 0
for word in str1:
    if word in 'aeiou':
        n += 1
print(n)
print('\n')

# 과제 1-1
n = 1
sum = 0

while n <= 1000:
    if n % 3 == 0:
        sum += n
    n += 1
print(sum)
print('\n')

# 과제 1-2
n = 10
while n > 0:
    print('*'*n)
    n -= 1
print('\n')


# 과제 1-3
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for score in A:
    if score >= 50:
        sum += score
        
print(sum)
print('\n')

# 과제 2-1
for i in range(1, 101):
    print(i)
print('\n')

# 과제 2-2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in A:
    sum += score
print(sum/len(A))
print('\n')

# 과제 2-3
numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n % 2 == 1]
print(result)