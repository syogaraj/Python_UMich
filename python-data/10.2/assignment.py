from pip._vendor.distlib.compat import raw_input

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counter = dict()
result = []

for line in handle:
    if line.startswith("From "):
        counter[(line.rstrip().split(" ")[6].split(":")[0])] = counter.get((line.rstrip().split(" ")[6].split(":")[0]),0) + 1

for k,v in counter.items():
    result.append((k,v))

result.sort()
for k,v in result:
    print(k,v)
