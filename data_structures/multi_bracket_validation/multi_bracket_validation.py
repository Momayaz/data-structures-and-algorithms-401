
def multi_bracket_validation(input_str):
    open_brackets = ["[","{","("]
    close_brackets = ["]","}",")"]
    temp_list = []
    for char in input_str:
        if char in open_brackets:
            temp_list.append(char)
        elif char in close_brackets:
            char_index = close_brackets.index(char)
            if ((len(temp_list) > 0) and (open_brackets[char_index] == temp_list[len(temp_list)-1])):
                temp_list.pop()
            else:
                return False
    if len(temp_list) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(multi_bracket_validation("{{hi)}}"))
