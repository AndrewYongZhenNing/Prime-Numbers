import numpy as np
import math

print "Welcome to the Mersenne Prime programme, please select a lower and an upper boundary to begin the search: \n"

p = input("ENTER LOWER BOUNDARY: ")
upper_boundary = input ("ENTER UPPER BOUNDARY: ")
lower_boundary = p

mersenne = 2**p - 1
mersenne_prime = []
power = []

file_title_1 = str(p)
file_title_2 = str(upper_boundary)

while p < upper_boundary+1:

    mersenne = 2**p - 1

    print "Number under evaluation: ", mersenne , "\t Power: ", p, "\t Terminating point: ", 2**upper_boundary - 1

    divisor = 2
    end_divisor = math.sqrt(mersenne)

    if mersenne == 3:
        mersenne_prime.append(mersenne)
        power.append(p)

    else:
        while divisor < end_divisor+1:

            remainder = mersenne%divisor

            if remainder != 0:

                divisor += 1

                if divisor == end_divisor+1 and remainder!=0:

                    mersenne_prime.append(mersenne)
                    power.append(p)

                    print "Ping! ", mersenne, " is a Mersenne prime!"
                    break

            elif remainder == 0:
                break

        # divisor +=1

    p +=1


print "\nCalculation completed. \nBetween ",  lower_boundary, " to" , upper_boundary, ", there are ", len(mersenne_prime), " of Mersenne primes."

number = np.linspace(1,len(mersenne_prime),len(mersenne_prime))


f = open("MersennePrime" + file_title_1 + "-" + file_title_2 + ".dat","w")
f.write("Power " + "    " "Mersenne Prime")

for p, prime in zip(power,mersenne_prime):
    f.write("\n" + str(p) + "    " + str(prime))

f.close()
