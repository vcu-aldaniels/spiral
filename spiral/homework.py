# declare function sum
 def sum(dim):
  n = (dim - 1) /2;#find n 
  use the formula defined above
  x = (3 + 2 * n * ( 8 * n * n + 15 * n +13)) /3
  return x

 def main():
  # call the function and print the value
   diagonal = sum(5)
   print (diagonal)

 main()