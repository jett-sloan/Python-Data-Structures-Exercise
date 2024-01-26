def read_file_list(filename):
    result = []
    file = open(filename,'r')
    for line in file:
        result.append('-'+ line.strip())
    return result

    
   
lines = read_file_list("/home/jettsloan/css/python-ds-practice/fs_5_read_file_list/cats")

print(lines)