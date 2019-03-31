import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
METHOD = "GET"

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)


# -- The number of total jokes about Chuck Norris available at the database
ENDPOINT = "/jokes/count"

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None)

# -- Wait for the server's response
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Read the response's body
data1 = r1.read().decode("utf-8")

jokes = json.loads(data1)

num_jokes = jokes['value']
print('The total number of jokes in the database is {}\n'.format(num_jokes))


# -- The number and names of the different categories
ENDPOINT = "/categories"

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None)

# -- Wait for the server's response
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Read the response's body
data1 = r1.read().decode("utf-8")

category = json.loads(data1)

num_cat = len(category['value'])
print("The number of categories is: {}. Categories:".format(num_cat))
for elements in category['value']:
    print(elements)

# A random joke
ENDPOINT = "/jokes/random"

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None)

# -- Wait for the server's response
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Read the response's body
data1 = r1.read().decode("utf-8")

random_joke = json.loads(data1)
joke = random_joke['value']['joke']
print("\nRandom joke:")
print(joke)
