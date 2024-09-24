squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print(type(squares))
for i, v in enumerate (squares): #많이 쓰는 표현
    print("{}는 {}".format(i, v))