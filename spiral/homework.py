def spiralize(number):
    start = time.time()

    last_number = 501*501
    
    odd_numbers = xrange(1,last_number+1,2)

    i = 0

    gap = 1

    number = 1

    while odd_numbers[i] != last_number:
        for j in xrange(4):
            i+= gap
            solution += odd_numbers[i]
        gap += 1

    return_value = 1
    
    end = time.time()

    return return_value