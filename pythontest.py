user_coeffs = []
degree = int(input("What is the degree of your polynomial: "))
for i in range(degree+1):
    a = str(input("What is x^" + str(i) + " coefficient: "))
    if "/" in a:
        a=a.split("/")
        print("fraction")
        user_coeffs.append(float(a[0])/float(a[1]))
    else:
        user_coeffs.append(float(a))
print(user_coeffs)