class skip:
    # open the text file in read mode
    with open('skiplist.txt', 'r') as file:
        # read the contents of the file
        contents = file.read()

        # split the contents of the file into a list of strings, using a comma as the delimiter
        skiplist = contents.split(',')

        # convert the list of strings to a list of integers
        skiplist = [str(x) for x in skiplist]

    # print the list of values
    print(skiplist)
