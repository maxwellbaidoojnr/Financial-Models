
rate = float(input("Enter  the rate: "))
time = float(input("Enter the time: "))
principal = float(input("Enter the principal: "))

amount = principal *  (pow((1 + rate/100),time))
ci  =  amount  -  principal
print("Compound  interest  is   ",ci)