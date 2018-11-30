mynum = 2
mynum2 = 2
testing_number = int(2)
is_prime = True
my_list = [2,3]
while True:
    for i in my_list:
        if testing_number % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(testing_number)
        print("")
        my_list.append(testing_number)
    else: 
        is_prime = True
    testing_number = testing_number + 1
    mynum = 2
    mynum2 = 2
