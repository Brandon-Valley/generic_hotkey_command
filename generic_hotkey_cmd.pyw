
def write(lines, filePath, write_mode = 'overwrite'):

    
    # convert to str
    if type(lines) == list or type(lines) == tuple:
        str_converted_lines = []
        for line in lines:
            str_converted_lines.append(str(line))
    else:
        str_converted_lines = [str(lines)]
    
    # write lines to file
    if   write_mode == 'overwrite':
        writeFile = open(filePath, "w") 
    elif write_mode == 'append':
        writeFile = open(filePath, "a")

    for line_num, line in enumerate(str_converted_lines):
        writeFile.write(line)
        
        # do not write newline if you just wrote the last line
        if line_num != len(str_converted_lines) - 1:
            writeFile.write('\n')
 
    writeFile.close() #to change file access modes 


write(['sfs'], 'ran.txt')
from win32gui import GetWindowText, GetForegroundWindow
focus = GetWindowText(GetForegroundWindow())
write([focus], 'test.txt')

import keyboard


# print('hi')

# clone 3 st or 2 if you click in box
# sm 2 if you click in box 14 tabs if not

# Before running this script you must click in the Local Relative Path text box 
# Will run shift + Tab twice, copy the remote url, Tab twice,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


keyboard.press_and_release('tab', 1)
keyboard.press_and_release('tab', 1)
keyboard.press_and_release('tab', 1)
keyboard.press_and_release('tab', 1)

