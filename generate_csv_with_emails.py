'''
Script generates a .csv file with random email addresses.
'''
import csv
import random
import string

def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(letters) for i in range(stringLength))


if __name__ == '__main__':
    DOMAIN = '@ec2key.com'  # domain
    ROWS = 500              # number of rows in csv file
    LENGTH = 15             # local part length

    outputFile = open('output.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['email'])

    for x in range(ROWS):
        strng = randomString(LENGTH) + DOMAIN
        outputWriter.writerow([strng])

    outputFile.close()

