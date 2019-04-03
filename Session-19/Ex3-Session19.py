import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Introduce the name of a Github user: ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data
name = user['name']
GITHUB_ID2 = GITHUB_ID+"/repos"

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID2, None, headers)

# -- Wait for the server's response
r2 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json2 = r2.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
repositories = json.loads(text_json2)

list_repos = ''
for info in repositories:
    rep = info['name']
    list_repos += rep + '\n'

ENDPOINT2 = '/repos/'
GITHUB_ID3 = GITHUB_ID + '/2018-19-PNE-practices/contributors'

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT2 + GITHUB_ID3, None, headers)

# -- Wait for the server's response
r3 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json3 = r3.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
commits = json.loads(text_json3)
contributions = commits[0]['contributions']


print()
print("Name: {}\n".format(name))
print('Repos: \n{}'.format(list_repos))
print("The total number of commits to the 2018-19-PNE-repo is", contributions)
