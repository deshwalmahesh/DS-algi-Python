def selection(lis, length):
    
    for i in range(length-1):
        min = lis[i]
        index = -1
        for j in range(i+1, length):
            if lis[j] < min:
                min = lis[j]
                index = j
        
        if min < lis[i]:
            temp = lis[i]
            lis[i] = min
            lis[index] = temp
    
    print(lis)
