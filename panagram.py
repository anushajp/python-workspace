def panagram (input_string):
    alphabet_string = "zxcvbnmlkjhgfdsaqwertyuiop"
    for i in alphabet_string:
        if i not in input_string:
            print("Input string is not a panagram")
            return
    print("Input string is a panagram")
    return

input_string = 'qwertyuiopvbn'
input_string1 = 'qwertyuiopasdfghjklzxcvbnm'
panagram(input_string) # output:- Input string is not a panagram
panagram(input_string1) # output:- Input string is a panagram
