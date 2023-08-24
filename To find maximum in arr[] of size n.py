#To find maximum in arr[] of size n
#function to find max in arr
def largest(arr, n):
    #initialize max element
    max=arr[0]
    
    #traverse array elements from second and compare every element with current max
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

#driver code
if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    #Calculating length of an array
    ans=largest(arr, n)
    #display max
    print("Largest in given array is:",ans)