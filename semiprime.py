#run with python 3
from primepriv import isprime #importing my isprime function from another file

import math
#Testing if input is valid or not
while True:

	try:

		lower = int(input("lower range: "))

		upper = int(input("upper range: "))
		#if the user puts in valid numbers
		if upper > 0 and lower > 0 and upper > lower:
			#only continue if the user puts in valid input
			break
		else:
			print("Please put in positive numbers and make sure that the upper range is larger than the lower range")

	except:
		#Throw an exception if the users does not put in an input
		print("Please put in numbers")
#semi prime function
def semiprime (upper, lower, primes):

    #array which will hold the semi primes
    semiprimes = []
    #squarert is the square root of the upper value given
    squarert = math.sqrt(upper)
    #iterate from 0 to the amount of primes that we have calculated
    for x in range(0, len(primes)):
    	#if we are at a primes that is larger than the square root of the upper, we can stop calculating (rest of them will be above the given range)
        if (primes[x] > squarert):

            break
        #find the upper range of primes that we need for this particular number and round down so we are inclusive
        upperprimerange = upper // primes[x]
        #find the lower range of primes that we need for this number (add 1 because we need to round up to)
        lowerprimerange = lower // primes[x] + 1
        #iterate through from the current prime to the rest of them
        for i in range(x, len (primes)):
            #if this prime is above the range, we can continue to the next number
            if primes[i] > upperprimerange:

                break
            #if the prime is in the range, calculate the semi prime and add it to the list
            if primes[i] >= lowerprimerange:
                #calculate the semiprime
                product = primes[x] * primes[i]
                semiprimes.append(product)

    return semiprimes
#largestprime is the largest possible prime that we need for this calculation (half of the upper range)
largestprime = math.floor(upper/2)
#primes is a list of the primes that we need in the calculation
primes = isprime(largestprime)#isprime function takes a parameter of the upper range of primes
#call semiprimes function
semiprimes = semiprime(upper, lower, primes)
#sort the semiprimes in ascending order
semiprimes.sort()
#print the semi primes
print("Number of semi primes in range: " + str(len(semiprimes)))
print ("Semi primes in range are: " + str(semiprimes))