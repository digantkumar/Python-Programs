# Digant Kumar

#Computing the area of the triangle, given the length of its three sides
def triangle_area(s1,s2,s3):
    s = (s1+s2+s3)/2
    area = (s* (s-s1)* (s-s2)* (s-s3)) ** 0.5
    return area

#Computing the factorial of the given number
def factorial(number):
    fact = 1
    if number<0:
        print("A negative number entered")
        number = int(input("Please enter a non-negative number:"))
    if number == 0:
        return fact
    else:
        for i in range(1,number+1):
            fact = fact * i
        return fact

#Calculating the quadractic roots of the given equation
def quadratic_roots(a,b,c):
    discriminant = (b ** 2 - 4 * a * c)
    #print(discriminant)
    if discriminant > 0:
        root1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        root2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        return root2, root1
    if discriminant == 0:
        root1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        print("Both the roots are same: ", end="")
        return root1
    else:
        return "The equation has no roots"

#Calculating the value of exp_x according to the given conditions.
def exp_approx(number):
    fact = 1
    total = 0
    for i in range(1,101):
        k_fact = fact*i
        numerator = number**i
        exp_x = total + numerator/k_fact
    return exp_x

print(exp_approx(2))