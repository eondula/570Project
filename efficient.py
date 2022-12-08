input_file_path = "input2.txt"
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
def get_alpha(x):
    '''Match letters
    x -- char 
    
    return -- alpha int
    '''
    
    if x == 'A':
        return 0
    elif x == 'C':
        return 1
    elif x == 'G':
        return 2
    elif x == 'T':
        return 3
      
def alignment_cost_2(X, Y, alpha_list, delta):
    '''
    alpha -- 2D list
    x -- char
    y -- char
    return -- value
    '''
    X_length = len(X)
    Y_length = len(Y)
    
    # cols (x) by rows (y) =>
    OPT = [[0 for x in range(X_length + 1)] for y in range(Y_length + 1)]
    # print(X_length, "\n", Y_length, "\n", OPT)

#     Base cases/Initialize
    OPT[0][0] = 0
    
    # To fill the rows we need the columns to change, we are moving from col 0 ... x_len; going column by column; fixed/initialize on row
    for col in range(X_length + 1):
        # print(col)
        OPT[0][col] = col * delta
        # print(OPT, np.shape(OPT))
    
    # To fill the col we need the row to change, we are moving from row 0 ... y_len; going row by row; fixed/initialize on col    
    for row in range(Y_length + 1):
        # print(col)
        OPT[row][0] = row * delta
        # print(OPT)

    # print("\n", np.array(OPT).T)
#         Recurrence Formula
    # print(OPT)
    
    # i reps the colums; outter loop reps cols
    for i in range(1, X_length + 1):
        # j reps the rows; inner loop reps rows
        for j in range(1, Y_length + 1):
            # print(i, j)
            x_i = X[i - 1]
            y_j = Y[j - 1] 
            # print(x_i, y_j)
            # print("before:, ", OPT)
            # print(get_alpha(x_i), get_alpha(y_j))
            alpha = alpha_list[get_alpha(x_i)][get_alpha(y_j)]
            # alpha = alpha_list[get_alpha(y_j)][get_alpha(x_i)]
            # print(alpha)
            # print(alpha + OPT[i - 1][j - 1],
            #             delta + OPT[i - 1][j],
            #             delta + OPT[i][j - 1])
            OPT[j][i] = min(
                        alpha + OPT[j - 1][i - 1],
                        delta + OPT[j - 1][i],
                        delta + OPT[j][i - 1]
            )
            # print("after:, ", OPT)
            # print()  
    # print(OPT)
    # return OPT[X_length][Y_length]
    return OPT[len(Y)][len(X)]
    # return OPT[i][j]

X = generate_string(ns)[0]
Y = generate_string(ns)[1]

alpha_list = [
    [0, 110, 48, 94],
    [110, 0, 118, 48],
    [48, 118, 0, 110],
    [94, 48, 110, 0]
]
print("Alignment cost: ",alignment_cost_2(X, Y, alpha_list, 30))
  
