#IEEE task 0 Q3

#creating the funtion to check if the number is prime or not
def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

#accepting the input from the user
N = int(input("Enter the number till which to check for primes: "))

#printing the prime numbers from 2 to N
for i in range(2, N):
    if is_prime(i):
        print(i , end=" ")

#When does the else block associated with a for loop execute?
#The else bkock associated with the for loop executes when the for loop doesn't encounter a break/return statement.