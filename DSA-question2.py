#The complexity of this algorithm is constant because the steps required to complete the execution of an algorithm remain constant, 
# irrespective of the number of inputs. The constant Complexity is denoted by (O(c)) where c can be any constsnt number.

def naturalnumbers(list2):
    k=2
    list2.sort(reverse=True)
    list2=sum(list2[0:k])
    return list2

print(naturalnumbers([2,9,3,10,50]))