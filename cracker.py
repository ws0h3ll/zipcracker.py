import zipfile
import time
filename = raw_input('path to file : ')
with open(filename, 'r') as f:
    a = f.read()
    b = a.split()
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password) #try extract all files with the password from the bruteforce

        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception, e:
        pass
zippath = raw_input('path to the zip : ')
zipfilename = zippath #takes where the zip file is

zip_file = zipfile.ZipFile(zipfilename) #uses zipfile module to connect to the zipfile
i = 0 #iteration variable
while i < len(b):
    time.sleep(0.001) #not needed but slows it down to reduce possible crashes
    password = b[i] #sets the attempting pass
    print "Trying: %s" % password #tells us whats being used
    if extractFile(zip_file, password): # runs the function ran above to try extract Files
    #if it works the below code is run
        print '*' * 20
        print 'Password found: %s' % password #tells us the password
        print 'Files extracted...'
        exit(0) # ends the program
    i += 1 #else increments the counter for the array to itterate again

print 'Password not found.' #if it doesnt work
