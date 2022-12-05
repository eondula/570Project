input_file_path = "input.txt"


def get_final_string(k, v):
    s = k
    for i in v:
        new_str = s[:i + 1] + s + s[i + 1:]
        s = new_str
    return s


def generate_string(my_dict):
    f_strings = []
    for i, (k, v) in enumerate(my_dict.items()):
        f_strings.append(get_final_string(k, v))
    return f_strings


def get_strings_with_gaps(str_list):
    # s1 = str_list[0]
    # s2 = str_list[1]

    return str_list


# {"ACTG": [3, 6, 1], 1: [1, 2, 9]}
# Detravious'
def alignment_cost(X, Y):
    '''
    X -- list
    Y -- list
    return -- int
    '''
    copy_X = X
    copy_Y = Y

    alpha = [[0 for x in range(4)] for y in range(4)]
    # print(alpha[1][1])
    alpha[0][1] = 110
    alpha[0][2] = 48
    alpha[0][3] = 94

    alpha[1][0] = 110
    alpha[1][2] = 118
    alpha[1][3] = 48

    alpha[2][0] = 48
    alpha[2][1] = 118
    alpha[2][3] = 110

    alpha[3][0] = 94
    alpha[3][1] = 48
    alpha[3][2] = 110

    print(alpha)

    dict = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    # print("A in dict:", dict[0])
    delta = 30

    # Create an empty 2D matrix
    OPT = [[0 for x in range(len(X))] for y in range(len(X))]
    # print(OPT)

    OPT[0][0] = 0

    print()

    for i in range(len(X)):

        min_costs = []
        for j in range(len(Y)):

            # OPT[i][0] = k * delta
            # OPT[0][j] = k * delta

            print(i, j)
            print()
            print("X[i] = ", X[i], "Y[j] = ", Y[j])
            # min_cost = min(i * delta + OPT[i - 1][j], i * delta + OPT[i][j - 1])
            # print(min_cost)

            if X[i] == Y[j]:
                print("cost: ", alpha[0][0], "i, j * d: ", i, j)
                min_cost = min(alpha[0][0] + OPT[i - 1][j - 1], (i * delta) + OPT[i - 1][j],
                               (j * delta) + OPT[i][j - 1])
                min_costs.append(min_cost)
                OPT[i][j] = min_cost
                print(OPT[i][j])


            elif (X[i] == dict[0] and Y[j] == dict[1]) or \
                    (X[i] == dict[1] and Y[j] == dict[0]) or \
                    (X[i] == dict[2] and Y[j] == dict[3]) or \
                    (X[i] == dict[3] and Y[j] == dict[2]):
                print("cost: ", alpha[1][0], "i, j * d: ", i, j)
                min_cost = min(alpha[1][0] + OPT[i - 1][j - 1], (i * delta) + OPT[i - 1][j],
                               (j * delta) + OPT[i][j - 1])
                print("min_cost = ", min_cost)
                min_costs.append(min_cost)
                OPT[i][j] = min_cost
                print(OPT[i][j])


            elif (X[i] == dict[0] and Y[j] == dict[2]) or \
                    (X[i] == dict[2] and Y[j] == dict[0]) or \
                    (X[i] == dict[1] and Y[j] == dict[3]) or \
                    (X[i] == dict[3] and Y[j] == dict[1]):
                print("cost: ", alpha[2][0], "i, j * d: ", i, j)
                min_cost = min(alpha[2][0] + OPT[i - 1][j - 1], (i * delta) + OPT[i - 1][j],
                               (j * delta) + OPT[i][j - 1])
                print("min_cost = ", min_cost)
                min_costs.append(min_cost)
                OPT[i][j] = min_cost
                print(OPT[i][j])


            elif (X[i] == dict[1] and Y[j] == dict[2]) or \
                    (X[i] == dict[2] and Y[j] == dict[1]):
                print("cost: ", alpha[1][2], "i, j * d: ", i, j)
                min_cost = min(alpha[1][2] + OPT[i - 1][j - 1], (i * delta) + OPT[i - 1][j],
                               (j * delta) + OPT[i][j - 1])
                print("min_cost = ", min_cost)
                min_costs.append(min_cost)
                OPT[i][j] = min_cost
                print(OPT[i][j])


            elif (X[i] == dict[0] and Y[j] == dict[3]) or \
                    (X[i] == dict[3] and Y[j] == dict[0]):
                print("cost: ", alpha[3][0], "i, j * d: ", i, j)
                min_cost = min(alpha[3][0] + OPT[i - 1][j - 1], (i * delta) + OPT[i - 1][j],
                               (j * delta) + OPT[i][j - 1])
                print("min_cost = ", min_cost)
                min_costs.append(min_cost)
                OPT[i][j] = min_cost
                print(OPT[i][j])
    print()
    print(min_costs)
    return OPT[i][j]


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

    # Getting the alignment cost. We initially assume that there will always be two strings i.e ["s1", "s2"]
    X = generate_string(ns)[0]
    Y = generate_string(ns)[1]
    alignment_cost(X, Y)

