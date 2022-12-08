input_file_path = "input.txt"
#print(input_file_path)
alpha_list = [
    [0, 110, 48, 94],
    [110, 0, 118, 48],
    [48, 118, 0, 110],
    [94, 48, 110, 0]]
delta_val = 30


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


def get_string_alignment(opt, str1, str2, delta):
  """
  return str1_alignment, str2_alignment
  """
  str1_alignment = []
  str2_alignment = []
  
  m = len(opt) # number of rows
  n = len(opt[0]) # number of cols
  print(m, n)
  # while i < m and j
  # # for i in range(m): # index of rows
  # #   for j in range(n-1,-1,-1): # index of cols
  #     # check all str1[]s, str2_alignment and str1_alignment for elif conditions
  #     # check three cases(subproblems) -> three neighbors in the matrix
  #     print(i, j)
  #     if (opt[i-1][j-1] + alpha_list[get_alpha(str1[])][get_alpha(str2[j+1])]) == opt[i][j]:
  #       str1_alignment.insert(0,str1[i-1]) 
  #       str2_alignment.insert(0,str2[j-1])
  #       # list.insert(index of the string,content)
  #       # lst = ["A"]
  #       # lst.insert(0,"B")
  #       # lst = ["B","A"] # reverse the string->string = string[::-1]
  #       # insert "C" in the index 1 -> ["B,"C,"A"] string.insert(1,"C")
  #       # result = "".join(lst) -> string
        
  #     elif opt[i-1][j] + delta_val == opt[i][j]:
  #       # str1_alignment.insert(0,str1[i-1])
  #       str2_alignment.insert(0, "_") 
   
        
  #     elif opt[i][j-1] + delta_val == opt[i][j]:
  #       str1_alignment.insert(0, "_") 
  #       # str2_alignment.insert(0, str2[j-1])
  
  i,j = m-1,n-1 # i corresponds to rows, j corresponds to cols
  # while i>=0 and j>=0: 
    
  #   #print(i, j)
  #   alpha_list[get_alpha(str1[i-1])][get_alpha(str2[j-1])]) == opt[i][j]:
  #     print("First if")
  #     str1_alignment.insert(0,str1[i-1]) 
  #     str2_alignment.insert(0,str2[j-1])
  #     i-=1
  #     j-=1
        
  #   elif opt[i-1][j] == opt[i][j]:
  #     print("Second if")
  #     str1_alignment.insert(0,str1[i-1])
  #     str2_alignment.insert(0, "_")
  #     i-=1
        
  #   elif opt[i][j-1]  == opt[i][j]::
  #     # opt[i][j-1] + delta_val == opt[i][j]:
  #     print("Third if", i, j)
  #     str1_alignment.insert(0, "_") 
  #     str2_alignment.insert(0, str2[j-1])    
  #     j-=1    

  # start at here
  while i>=0 and j>=0:
    # base case
    print(i, j)
    letterx = str1[j-1]
    lettery = str2[i-1]
    print(letterx, lettery)
    
    if i==0 and j==0:
      print("end")
      break
    
    # first row
    elif i==0:
      # go left
      print("go left")
      # insert a gap in str2_alignment
      str1_alignment.insert(0,letterx)
      str2_alignment.insert(0,'_')
      j-=1
      
    # first col
    elif j==0:
      # go up
      print("go up")
      # insert a gap in str1_alignment
      str1_alignment.insert(0,'_')
      str2_alignment.insert(0,lettery)
      i-=1
      
    else: # compare opt[i-1][j-1]+alphalist,opt[i-1][j],+delta,opt[i][j-1]+delta
      if (opt[i-1][j-1] + alpha_list[get_alpha(str1[j-1])][get_alpha(str2[i-1])]) == opt[i][j]:
        print("go up left")
        str1_alignment.insert(0,letterx) 
        str2_alignment.insert(0,lettery)
        i-=1
        j-=1
      elif opt[i-1][j] + delta_val == opt[i][j]:
        print("go up")
        str1_alignment.insert(0,"_")
        str2_alignment.insert(0, lettery)
        i-=1
      else:
        print("go left")
        str1_alignment.insert(0, letterx) 
        str2_alignment.insert(0, "_")    
        j-=1 
  s1,s2 = "".join(str1_alignment),"".join(str2_alignment)
  return s1, s2
  
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
      
  #print(generate_string(ns))

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
    return OPT[len(Y)][len(X)], OPT
    # return OPT[i][j]

X = generate_string(ns)[0]
Y = generate_string(ns)[1]
# X = "ACTG"
# Y = "TATT"

cost, opt = alignment_cost_2(X, Y, alpha_list, delta_val)
print(cost)
#print(opt)
print(get_string_alignment(opt, X, Y, delta_val))
  
