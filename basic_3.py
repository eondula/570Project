input_file_path = "input.txt"
print(input_file_path)
with open(input_file_path) as f:
  l2write = []
  
  lines = f.readlines()
  strings = []
  for i in range(len(lines)):
    if lines[i].strip().isdigit() == False:
      l2write.append(0)
      strings.append(lines[i].rstrip())
    else:
      l2write[-1] += 1
    print(l2write)

  print(l2write)
  print(strings[0])

  s1 = strings[0]
  s2 = strings[1]
  j = l2write [0]
  k = l2write [1]
  
  