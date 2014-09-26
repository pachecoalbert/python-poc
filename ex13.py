from sys import argv
script, user_name = argv
prompt = '> '

print "Hi %s, Im the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print """
Alright, so you saide %r about liking me.
You live in %r. Not sure where that is.
""" % (likes, lives)

