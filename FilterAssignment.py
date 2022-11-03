import os

input_path = "" # Folder that contains all the assignments, that were handed in
output_path = "" # Folder the filtered assigments will be put in

group_string = "" # Prefix of group i.e. "G2"
name_list = [] # List of possible names in filename
search_args = [group_string] + name_list

directory_list = os.listdir(input_path)
for elem in directory_list:
    if os.path.isfile(elem):
        pass
    else:
        file_list = os.listdir(input_path + "\\" + elem)
        if any(keyword in filename for filename in file_list for keyword in search_args)

