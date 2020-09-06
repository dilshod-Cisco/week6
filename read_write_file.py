filename = 'data/inputData.txt'

with open(filename) as input_data: # we use 'with' cos we don't need deal with stock overflow.
    counter = 1
    print(" 1).reading  line by line: ")
    for line in input_data:
        print("line: ", counter, line)


    # print("2).Reading the whole content and assigning to a variable")
    # contents = input_data.read()
    # print(contents)

    # print("3). read line by line using readlines(), return as list of lines")
    # # if you choose this way you can loop lines outside of WITH statement
    # # lines = input_data.readlines() - reading line by line

print("Reding a inputData.txt file completed")


# WRITHING TO THE FILE
with open(filename, 'a') as file_object: # use 'w' to override, 'a' to append
    file_object.write(" I love programming.\n ")
    file_object.write(" I love Python.\n ")