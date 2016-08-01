import numpy as np
import matplotlib.pyplot as plt

# ALL PRIMES
starting_number = 2
upper_boundary =  input("ENTER UPPER BOUNDARY: " ) # if you want input from terminal, do not put ampersand & in the command as anything AFTER the execution of the code is regarded as writing on the terminal
upper_boundary = int(upper_boundary)

prime_number = []
mersenne_prime = []

while starting_number < upper_boundary+1:
    divisor = 2
    halfway_point= starting_number/2

    if halfway_point == 1:
        prime_number.append(starting_number) # includes the first two prime numbers: 2 and 3

    else:
        print "Current number under evaluation: ", starting_number
        while divisor < halfway_point+1:

            if starting_number%divisor != 0: # there is a remainder
                divisor +=1
                if divisor == halfway_point and starting_number%divisor != 0:
                    prime_number.append(starting_number)

            elif starting_number%divisor == 0: # some number besides 1 and the number itself divides into the number, therefore a composite number
                break



    starting_number += 1

# MERSENNE PRIME
p = 1
mersenne = 2**p - 1
for prime in prime_number:
    if mersenne == prime:
        mersenne_prime.append(mersenne)
    elif mersenne != prime and mersenne < prime+1:
        p +=1



x = np.linspace(1,len(prime_number),len(prime_number))
x_mersenne = np.linspace(1,len(mersenne_prime),len(mersenne_prime))

print mersenne_prime

plt.figure()
plt.grid()
plt.title("Prime Numbers")
plt.xlabel('Number')
plt.ylabel('Prime Numbers')
plt.xlim(0,x[-1]+1)
plt.scatter(x, prime_number, color = 'b', label = 'All Primes')
plt.plot(x, prime_number, color = 'b')
plt.scatter(x_mersenne, mersenne_prime, color = 'r', label = 'Mersenne Primes')
plt.legend()
plt.show()
