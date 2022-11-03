import os
from shutil import copy

## CHANGE IO PATHS HERE
input_path = "" # Folder that contains all the assignments, that were handed in
output_path = "" # Folder the filtered assigments will be put in

## CHANGE SEARCH ARGUMENTS HERE
group_string = [] # Prefix of group i.e. "G2", "2"
name_list = [] # List of possible names in filename
search_args = group_string + name_list

# recursive dfs function to find files and copy them to destination folder if search criteria is matched
def file_check(path):
    directory_list = os.listdir(path)
    
    for dir in directory_list:
        new_path = path + "/" + dir
        
        if os.path.isfile(new_path) and any(keyword in dir.split("_") for keyword in search_args):
                print(dir)
                copy(new_path, output_path)
        elif not os.path.isfile(new_path):
            file_check(new_path)

file_check(input_path)
