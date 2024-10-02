def sort_string(s):
    char = list(s)
    n = len(char)

    for i in range(n):
        for j in range(0,n-i-1):
            if(char[j]>char[j+1]):
                char[j],char[j+1] = char[j+1],char[j]

    sorted=''.join(char)
    return sorted

s = input("enter")
sorted1 = sort_string(s)
print(sorted1)