class ListLenthExeption(Exception):
    pass
def check_list_len(l:list):
    if len(l)>5:
        raise ListLenthExeption("arry length less then 5")
    return True

arr=[34,5,7,8,9,56]
print(check_list_len(arr))