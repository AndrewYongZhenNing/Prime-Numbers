import numpy as np

print "Welcome to the Mersenne Prime programme, please select a lower and an upper boundary to begin the search: \n"

p = input("ENTER LOWER BOUNDARY: ")
upper_boundary = input ("ENTER UPPER BOUNDARY: ")

mersenne = 2**p - 1
mersenne_prime = []

file_title_1 = str(p)
file_title_2 = str(upper_boundary)

while p < upper_boundary+1:

    mersenne = 2**p - 1

    print "Number under evaluation: ", mersenne , "\t Power: ", p, "\t Terminating point: ", 2**upper_boundary - 1

    divisor = 2
    end_divisor = int(np.sqrt(mersenne))

    if mersenne == 3:
        mersenne_prime.append(mersenne)

    else:
        while divisor < end_divisor+1:
            print 'Current divisor: ', divisor, '\t', 'Divisor terminating point: ', end_divisor, "\t Terminating point: ", 2**upper_boundary - 1
            remainder = mersenne%divisor

            if remainder != 0:

                divisor += 1

                if divisor == end_divisor+1 and remainder!=0:

                    mersenne_prime.append(mersenne)

                    print "Ping! ", mersenne, " is a Mersenne prime!"
                    break

            elif remainder == 0:
                break

        # divisor +=1

    p +=1


print "\nCalculation completed. \nBetween ",  p, " to" , upper_boundary, ", there are ", len(mersenne_prime), " of Mersenne primes."

number = np.linspace(1,len(mersenne_prime),len(mersenne_prime))


f = open("MersennePrime" + file_title_1 + "-" + file_title_2 + ".dat","w")
f.write("Number" + "    " + "Mersenne Prime")

for number, prime in zip(number,mersenne_prime):
    f.write("\n" + str(number) + "    " + str(prime))

f.close()
