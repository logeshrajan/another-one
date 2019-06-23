def swap_case(s):
    output_list = []
    output_string=""
    for i in s:
        if i.isupper():
            output_list.append(i.lower())
        elif i.islower():
            output_list.append(i.upper())
        else:
            output_list.append(i)
    output_string="".join(output_list)
    return output_string

# import string
# print string.swapcase(raw_input())


