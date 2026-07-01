# Read from the file file.txt and print its transposed content to stdout.
f = open("file.txt", "rt")
d = f.read()
f.close()
lines = list(map(lambda x: x.split(" "), d.split(" ")))
newLines = []
for i in range(len(lines[0])):
print(" ".join([x[i] for x in lines]))