import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
METHOD = "GET"

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)


# -- Capital weather information
cap = True
woeid = 0
capital = ""
while cap:
    capital = input("Please, enter a capital city: ")
    ENDPOINT = "/api/location/search/?query={}".format(capital)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None)

    # -- Wait for the server's response
    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    wheather = json.loads(data1)

    if len(wheather) == 0:
        print("The capital introduced does not exist.")
    else:
        cap = False
        woeid = wheather[0]['woeid']

ENDPOINT = '/api/location/{}/'.format(woeid)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None)

# -- Wait for the server's response
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Read the response's body
data1 = r1.read().decode("utf-8")

info = json.loads(data1)

time = info['time']
sunset = info['sun_set']
temp = info['consolidated_weather'][0]['the_temp']

print("The current time in {} is {}".format(capital, time))
print("The temperature in {} is {}".format(capital, temp))
print("The sunset in {} is {}".format(capital, sunset))
