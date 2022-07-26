# 연습문제1
with open('words1.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for i in words:
        if len(i.strip('\n')) <= 10:
            count += 1
    
print(count)

print()

# 심사문제1
with open('words2.txt', 'r') as file:
    line = file.readline()
    if line == None:
        print('No letters.')
    wlist = line.split()
    for i in wlist:
        i =  i.strip(',.')
        if i.count('c'):
            print(i)
