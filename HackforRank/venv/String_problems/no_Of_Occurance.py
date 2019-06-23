def count_substring(string, sub_string):
    res=0
    for i in range (0,len(string)-len(sub_string)+2):
        if string[i:i+len(sub_string)] == sub_string:
            res+=1
    return res