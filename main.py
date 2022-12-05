# sample file
f = '''some text
120 130
1847 1853
other text
207 220
text
306 350
text with no numbers after
some other text
400 435
900 121
125 369'''

lines = f.split('\n')

line2write = []

for line in lines:
    if not line[0].isdigit():
        line2write.append(0)
        print(line)
    else:
        line2write[-1] += 1
print(line2write)