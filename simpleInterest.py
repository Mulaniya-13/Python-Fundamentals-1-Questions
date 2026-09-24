principal=input("Enter principal amount: ")
rate=input("Enter rate of interest: ")
time=input("Enter time: ")

principal=float(principal)
rate=float(rate)
time=float(time)

SI = (principal*rate*time)/100

print(SI)