from pip._vendor.distlib.compat import raw_input

# fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
sum = 0
cnt = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sum += float(line[line.find(':')+1:].strip())
    cnt += 1
print("Average spam confidence: " + str(sum/cnt))
