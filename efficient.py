#
input_file_path = "SampleTestCases/input1.txt"
with open(input_file_path) as f:
    lines = f.readlines()
    #print(lines)
    for i in range(len(lines)):
        print((lines[i].isdigit()), i)
        # if(lines[i].isdigit()):
        #     print(lines[i], i)

        # if(i == 0):
        #     print("This is a string", lines[i], i)
        #
        # else:
        #     print("This is integer", lines[i], i)
        #

