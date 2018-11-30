
previousNumber = 3
twoNumbersBack = 2
fibNumber = 0
temp = 0
while True:
    temp = previousNumber
    previousNumber = fibNumber    
    twoNumbersBack = temp
    fibNumber = previousNumber + twoNumbersBack
    print(fibNumber)
