import re

name = "regex_sum_167246.txt"
handle = open(name)

sum = 0

for line in handle:
    for num in re.findall(r'\d+',line):
        sum += int(num)

print(sum)
