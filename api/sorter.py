# open the text file in read mode
with open('all_rendered_shots.txt', 'r') as file:
    # read the lines of the file into a list
    lines = file.readlines()

    # sort the lines alphabetically
    lines.sort()

# open the same text file in write mode
with open('output.txt', 'w') as file:
    # write the sorted lines back to the file
    file.writelines(lines)
