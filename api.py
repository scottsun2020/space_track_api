import requests

#User information
username = "your_space_track_username"
password = "your_space_track_password"

#URI snippets
uriBase = "https://www.space-track.org"
requestLogin = "/ajaxauth/login"
#sample query; user input custom query will be updated soon
query  = "/basicspacedata/query/class/gp/EPOCH/>now-30/MEAN_MOTION/0.99--1.01/ECCENTRICITY/<0.01/format/tle"
siteCred = {'identity': username, 'password': password}


# use requests package to drive the RESTful session with space-track.org
with requests.Session() as session:
    # need to log in first. note that we get a 200 to say the web site got the data, not that we are logged in
    resp = session.post(uriBase + requestLogin, data = siteCred)
    if resp.status_code != 200:
        print('not working')


    # this query based on uriBase and custom query
    resp = session.get(uriBase + query)
    if resp.status_code != 200:
        print(resp)

#save read files into space_track.orb
with open("space_track.orb", "w") as f:
    f.write(resp.text)

#print statement to show the code works
print("It works!")
