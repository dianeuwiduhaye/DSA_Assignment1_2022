#This algorthim has a linear complexity because the steps required to complete the execution of an algorthm increase or decrease,
# linearly with the number of inputs. The Linear Complexity is denoted by (O(n)).



def duplicates(list1):
    ocurrence={}
    for number in list1:
        if number in ocurrence:
            ocurrence[number]+=1
        else:
            ocurrence[number]=1
    for number in list1:
        if ocurrence[number] % 2==0:
            return False
    
    return True



print(duplicates([1,3,2,2,5,2,5]))
print(duplicates([1,3,2,2,5,2]))

# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("duplicates()", number=1,globals=globals()))



