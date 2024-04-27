for value in range(1,5):
    print(value)

numbers= list(range(1,5))
print(numbers)

squares =[val**2 for val in range(1,10)]
print(squares)
print(squares[1:4])
print(f"{squares[-3:]}\n")

a=[ 1, 2, 3, 4]
b=a[:]
c=a
print(a)
print(b)
print(c)
a.append(11)
b.append(22)
c.append(33)
print(a)
print(b)
print(c)