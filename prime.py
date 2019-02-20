mynum = 2
mynum2 = 2
testing_number = int(2)
is_prime = True
my_list = [2,3]
old_average_distance = 1
average_distance = 3 - 2
current_loop = 0
difference_between_primes = 1
distances = [average_distance]

max_difference = 0

while True:
    current_loop = current_loop + 1
    for i in my_list:
        if testing_number % i == 0:
            is_prime = False
            break
    if is_prime == True:
        
        difference_between_primes = testing_number - my_list[len(my_list) - 1] 
        
        distances.append(difference_between_primes)
        average_distance = 0
        for l in distances:
            average_distance = average_distance + l
            if l >= max_difference: max_difference = l
        average_distance = average_distance / len(distances)
        my_list.append(testing_number)

        print "testing Number: ", testing_number, " Average Distance: ", average_distance, " Current distance: ", difference_between_primes, " max: ", max_difference
        

    else: 
        is_prime = True
    testing_number = testing_number + 1
    mynum = 2
    mynum2 = 2
