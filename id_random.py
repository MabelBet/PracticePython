import random
import string
random = ''.join([random(string.ascii_letters + string.digits) for n in range(6)])
print (random)