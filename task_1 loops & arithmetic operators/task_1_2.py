# function that computes
#@list: list of integers
def compute_sum_of_cubes(list):
    sum_cubes = 0
    # compute sum_1
    for element in list:
        sum_digits = 0
        for digit in str(element):
            sum_digits += int(digit)
        # print('element:', element, '; sum_digits', sum_digits)

        if not sum_digits % 7:
            # print ('sum_digits % 7: ', sum_digits % 7)
            sum_cubes += element
    return sum_cubes

# create list of cubes of uneven numbers from 0 to 1000
list = [i**3 for i in range(1000) if i%2 != 0]
#print(list[:10])
print('sum_cubes 1:', compute_sum_of_cubes(list))

# add 17 to each element of the previous list
list = [i+17 for i in list]
#print(list[:10])
print('sum_cubes 2:', compute_sum_of_cubes(list))