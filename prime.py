import numpy as np
import matplotlib.pyplot as plt

# ALL PRIMES
starting_number = input("ENTER LOWER BOUNDARY: ")
upper_boundary =  input("ENTER UPPER BOUNDARY: " ) # if you want input from terminal, do not put ampersand & in the command as anything AFTER the execution of the code is regarded as writing on the terminal
lower_boundary = starting_number
starting_number = int(starting_number)
upper_boundary = int(upper_boundary)

file_title_1 = str(starting_number)
file_title_2 = str(upper_boundary)

prime_number = []
mersenne_prime = []

while starting_number < upper_boundary+1:
    divisor = 2
    halfway_point= starting_number/2

    if halfway_point == 1:
        prime_number.append(starting_number) # includes the first two prime numbers: 2 and 3

    else:
        print "Current number under evaluation: ", starting_number, 'terminating point: ', upper_boundary
        while divisor < halfway_point+1:

            if starting_number%divisor != 0: # there is a remainder
                divisor +=1
                if divisor == halfway_point and starting_number%divisor != 0:
                    prime_number.append(starting_number)
                    print "Ping!", starting_number, " is a prime number. "

            elif starting_number%divisor == 0: # some number besides 1 and the number itself divides into the number, therefore a composite number
                break



    starting_number += 1




# MERSENNE PRIMES

p = 1
mersenne = 2**p - 1

while mersenne < prime_number[-1]+1:

    print "Mersenne under evaluation: ", mersenne

    for prime in prime_number:

        if prime == mersenne:

            mersenne_prime.append(prime)
            print "Ping!", prime, ' is a Mersenne prime.'

    p += 1
    mersenne = 2**p - 1

print "\nCalculation completed. \nBetween ",  lower_boundary, " to" , upper_boundary, ", there are ", len(prime_number), " of prime numbers."


number = np.linspace(1,len(prime_number),len(prime_number))

f = open("MersennePrime" + file_title_1 + "-" + file_title_2 + ".dat","w")
f.write("Number" + "    " + "Mersenne Prime")

for number, prime in zip(number,mersenne_prime):
    f.write("\n" + str(number) + "    " + str(mersenne_prime))

f.close()


def Plot(prime_number_list, mersenne_prime_list):

    x = np.linspace(1,len(prime_number_list),len(prime_number_list))
    # x_mersenne = np.linspace(1,len(mersenne_prime_list),len(mersenne_prime_list))
    x_mersenne = []

    plt.figure()
    plt.grid()
    plt.title("Prime Numbers")
    plt.xlabel('Number')
    plt.ylabel('Prime Numbers')
    plt.xlim(0,x[-1]+1)
    plt.ylim(-0.5,prime_number_list[-1]+100)

    for primes in prime_number_list:

        x_step = np.linspace(1,len(prime_number_list),len(prime_number_list))
        y_step = [primes]*len(x_step)

        plt.plot(x_step,y_step, color = 'darkgreen')

    for primes in mersenne_prime_list:

        x_index = prime_number_list.index(primes)
        x_mersenne.append(x[x_index])
        # y_step = [primes]*len(x_step)

        plt.plot(x_step,y_step, color = 'purple')

    plt.scatter(x, prime_number, color = 'b', label = 'All Primes')
    plt.plot(x, prime_number, color = 'b')
    plt.scatter(x_mersenne, mersenne_prime, color = 'r', label = 'Mersenne Primes')
    plt.legend()
    plt.show()


# Plot(prime_number,mersenne_prime)
