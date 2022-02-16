
def knap_sack(capacity, weight, value, n):

	# first Case
	if n == 0 or capacity == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack's capacity,
	# then this item cannot be included
	# in the optimal solution
	if (weight[n-1] > capacity):
		return knap_sack(capacity, weight, value, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max(
			value[n-1] + knap_sack(
				capacity-weight[n-1], weight, value, n-1),
			knap_sack(capacity, weight, value, n-1))
        

# end of function knap_sack


#Driver Code
value = [2500,1700,1200,3000,4100,2000,7000,7500]
weight = [5,3,1,6,8,4,11,12]
capacity = 20
n = len(value)
print(knap_sack(capacity, weight, value, n))