def spiralize(number):
      
    n = (number - 1) / 2
    
    x = (3 + 2 * n * (8 * n * n + 15 * n +13)) / 3
    
    return_value = 1

    return return_value

def sum():

  diagonal = spiralize(5)
  print (diagonal)

sum()