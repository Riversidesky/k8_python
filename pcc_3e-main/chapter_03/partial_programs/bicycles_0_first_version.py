bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(len(bicycles))
bicycles[1] = "genesis" #바꿔치기
##추가 -> insert, append
bicycles.append('canival')
bicycles.insert(1, 'canival')
del bicycles[0]
print(bicycles)
print(bicycles[-3].title())