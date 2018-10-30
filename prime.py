mynum = 2
mynum2 = 2
testing_number = 4
is_prime = True
while True:
    while mynum < testing_number:
        mynum2 = 2
        while mynum2 < (testing_number // 2) + 1:
            if mynum2 % testing_number == 0:
                is_prime = False
                break
            if mynum * mynum2 == testing_number:
                is_prime = False
            mynum2 = mynum2 + 1
        mynum = mynum + 1
    if is_prime == True:
        print(testing_number)
        
    else: 
        is_prime = True
    testing_number = testing_number + 1
    mynum = 2
    mynum2 = 2
