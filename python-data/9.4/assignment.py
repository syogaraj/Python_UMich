from pip._vendor.distlib.compat import raw_input

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counter = dict()

for line in handle:
    if line.startswith("From:"):
        email = line.rstrip().split(" ")[1]
        counter[email] = counter.get(email, 0) + 1

print(str(max(counter, key=counter.get)) + " " + str(counter[max(counter, key=counter.get)]))
# print(max([(v,k) for (k,v) in counter.items()])[1], max([(v,k) for (k,v) in counter.items()])[0])
