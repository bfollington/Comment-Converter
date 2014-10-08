import sys

filename = sys.argv[1]

f = open(filename, "ru")
s = ""

for line in f:
    if "//" in line and len(line) > 0:
        i = line.index("//")
        l = line[:i] 

        l += "/*" 
        comment = line[i + 2:-1] 
        comment.strip()
        comment = ' ' + comment + ' '
        l += comment + "*/\n"

    else:
        l = line

    s += l

f.close()

f = open(filename, "w+")
f.write(s)
f.close()