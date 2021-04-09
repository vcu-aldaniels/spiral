def spiralize(number):
      
    n = (number - 1) / 2
    
    x = (3 + 2 * n * (8 * n * n + 15 * n +13)) / 3
    
    return_value = x

    return return_value
    
def sum():

  diagonal = spiralize(501)
 
  print (diagonal)
  
sum()

