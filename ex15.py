from sys import argv

script, filename = argv

txt = open(filename)

print "Hers's your file %r:" % filename
print txt.read()

print "Thpe the filename again:"
file_again  = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

