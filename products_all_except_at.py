def get_products_of_all_ints_except_at_index(l):
	return [reduce(lambda x,y: x*y, l)/e for e in l]

def get_products_of_all_ints_except_at_index_2(l):
	return [reduce(lambda x,y: x*y, subl) for subl in [l[:idx]+l[(idx+1):] for idx,e in enumerate(l)] ]

def get_products_of_all_ints_except_at_index_3(l):
	return [reduce(lambda x,y: x*y, l[:idx]+l[(idx+1):]) for idx,e in enumerate(l)]

def get_products_of_all_ints_except_at_index_O_n(int_list):

	# we make a list with the length of the input list to
	# hold our products
	products_of_all_ints_except_at_index = [None] * len(int_list)

	# for each integer, we find the product of all the integers
	# before it, storing the total product so far each time
	product_so_far = 1
	i = 0
	while i < len(int_list):
	    products_of_all_ints_except_at_index[i] = product_so_far
	    product_so_far *= int_list[i]
	    i += 1

	# for each integer, we find the product of all the integers
	# after it. since each index in products already has the
	# product of all the integers before it, now we're storing
	# the total product of all other integers
	product_so_far = 1
	i = len(int_list) - 1
	while i >= 0:
	    products_of_all_ints_except_at_index[i] *= product_so_far
	    product_so_far *= int_list[i]
	    i -= 1

	return products_of_all_ints_except_at_index
