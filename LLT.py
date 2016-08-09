"""Lucas Lehmer Primality Test"""

import numpy as np

print "Welcome to Lucas-Lehmer Primality Test. \nPlease enter a low and an upper boundary to begin primality test."


p = input("ENTER LOWER BOUNDARY: ")
lower_boundary = p
upper_boundary = input("ENTER UPPER BOUNDARY: ")

file_title_1 = str(p)
file_title_2 = str(upper_boundary)

mersenne_prime = []


while p < upper_boundary+1:

    s = 4
    start = 0
    end = p-2

    mersenne = 2**p - 1

    print "Mersenne under evaluation: ", mersenne, "\t Terminating point: ", 2**upper_boundary - 1

    while start < end:

        s = s**2 - 2

        remainder = (s**2 -2)%mersenne

        if remainder == 0:
            mersenne_prime.append(mersenne)
            print "Ping! ", mersenne, " is a Mersenne Prime!"
            break

        elif remainder != 0:
            start +=1
            if remainder != 0 and start == end:
                break

    p +=1

print "\nCalculation completed. \nBetween ",  lower_boundary, " to" , upper_boundary, ", there are ", len(mersenne_prime), " of Mersenne primes."

f = open("MersennePrime" + file_title_1 + "-" + file_title_2 + ".dat","w")
f.write("Power " + "    " "Mersenne Prime")

for p, prime in zip(power,mersenne_prime):
    f.write("\n" + str(p) + "    " + str(prime))

f.close()
