
def insertShiftArray(arr,value):
    arr_middle = len(arr)//2
    if len(arr)%2 == 0:
        return(arr[:arr_middle] + [value] + arr[arr_middle:])
        
    else:
       return( arr[:arr_middle+1] + [value] + arr[arr_middle:])
       

