
file1 = open('File1.txt', 'r')
Lines = file1.readlines()
 
count = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
print('Total number of lines are {}'.format(len(Lines)))