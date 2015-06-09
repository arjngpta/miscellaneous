import os
i = 0
n = [1,2,3]
file_list = os.listdir(os.getcwd())
for file_name in file_list:
        i = i + 1
        if i in n:
                print "i is in n"
        else:
                print "i is not in n"
        print i
print n
