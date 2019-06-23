n = int(input())
integer_list = map(int, input().split())
tuples_list=tuple(integer_list)
print(hash(tuples_list))