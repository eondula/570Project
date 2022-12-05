input_file_path = "input.txt"
print(input_file_path)

def get_final_string(k, v):

  s = k
  for i in v:
    new_str = s[:i+1] + s + s[i+1:]
    s = new_str
  return s
  
def generate_string(my_dict):
  f_strings = []
  for i, (k, v) in enumerate(my_dict.items()):
    f_strings.append(get_final_string(k, v))
  return f_strings
  
with open(input_file_path) as f:
  l2write = []
  ns = {}
  lines = f.readlines()
  strings = []
  for i in range(len(lines)):
    if lines[i].strip().isdigit() == False:
      l2write.append(0)
      strings.append(lines[i].rstrip())
      ns[strings[-1]] = []
    else:
      l2write[-1] += 1
      ns[list(ns)[-1]].append(int(lines[i].rstrip()))
      
  print(generate_string(ns))

# {"ACTG": [3, 6, 1], 1: [1, 2, 9]}

# 

