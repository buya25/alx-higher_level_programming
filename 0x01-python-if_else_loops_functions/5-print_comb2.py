#!/usr/bin/python3

end_str = ", "

for i in range(0, 100):
    if i == 99:
        end_str = ""
    print("{:02d}".format(i), end=end_str)
print('')
