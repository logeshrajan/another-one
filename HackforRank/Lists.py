N = int(input())
input_Commands=[]
for i in range (0,N):
    input_Cmd = input()
    input_Commands.append(input_Cmd)
output_list = []
for i in input_Commands:
    sample_List = i.split()
    if len(sample_List)== 2:
        if sample_List[0] == "insert":
            output_list.insert(int(sample_List[1]), int(sample_List[2]))
    elif len(sample_List)<=2:
        if sample_List[0] == "remove":
            output_list.remove(int(sample_List[1]))
        elif sample_List[0] == "append":
            output_list.append(int(sample_List[1]))
    elif sample_List[0] == "print":
        print(output_list)
    elif sample_List[0] == "sort":
        output_list.sort()
    elif sample_List[0] == "pop":
        output_list.pop()
    elif sample_List[0] == "reverse":
        output_list.reverse()