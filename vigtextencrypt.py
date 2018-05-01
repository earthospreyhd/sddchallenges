#run with python 3
import os
#function for encrypt and decrypting using the ceasar cipher
def vig (status, key, inputtext):

	#declare a list with the length of the inputtext

    output = [None] * len(inputtext);

    #iterate over the length of the inputtext

    for x in range(0,len(inputtext)):

    	#set the index for the letter in the key that we are using to encrypt(needs to be in mod length of key so that we loop back around)
        index = x % len(key)
        #set the offset (number of letters/values to shift by) as the ascii value of the character
        offset = ord(key[index])

        #Set the letter of the output to be equal to the input letter plus or minus(depending on whether status
        # is 1 for encrypt or -1 for decrypt) the offset in modulo 255 (amount of ascii characters)

        output[x] = chr((ord(inputtext[x]) + offset*status) % 127)
    
    
    return (output)

#Loop to take input and make sure that it is valid

while True:

	try:
		#Take input of an int
		status = int(input("Please enter 1 if you want to encrypt a file or -1 if you want to decrypt a file: "))

		if status == 1 or status == -1:

			#if the input is valid, break out of the loop

			break

		else:

			#if the input is not valid, try again

			print("Please enter a valid number")

	except:
		#if the input is not a number retry
		print("Please enter a number")
#Loop to take input and make sure that it is valid
while True:

	try:
		#take an input of the file name
		filename = input("Enter the name of the file: ")
		#open the filestream
		file = open (filename)
		#break out of the loop if the file is valid
		break

	except:
		#Throw an exception if the file name is not valid
		print("That is not a valid file name\n")
		#continue back to the top of the loop

#take the input of the encryption key
key = input("Put in the key that you will use: ")
#take in the name of the file that they want to output to
outname = input("Enter the name of the file that you would like to store the text in: ")
#read the file
inputtext = file.read()
#call the encryption/decryption function
encrypt = vig(status, key, inputtext)
#Create the file with the users output name
output = open(outname, "w")
#Write the encrypted text to the file
output.write(''.join(encrypt))
print("Proccess complete")
#Loop so that the user can delete the original file if they wish
while True:

    deletefile = input("Enter 1 if you would like to keep the original file or 0 if you would like to delete it: ")

    if deletefile == '0':

        try:

            os.remove(filename)

            print("The original file '" + filename + "'' has been destroyed")

            break

        except:

            print("An error occurred when trying to delete the original file")

            break

    elif deletefile == '1':

        break

    else:

        print("Please enter a valid option")
