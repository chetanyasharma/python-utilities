import requests
print "tell me ur choice for input data"
print " type 'a' for address or 'l' for coordinates"
choice = raw_input("enter your choice")
if choice == "a" :
    address = raw_input("enter your address")
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyAJqyrvqqQ7TnPBjWugY5DsfAPXHgBQu5Q")
    print(response.content)
if  choice == "l" :
    latitude = int(raw_input("enter ur latitude"))
    longitude = int(raw_input("enter ur longitude"))
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latitude + "," + longitude + "&key=AIzaSyAJqyrvqqQ7TnPBjWugY5DsfAPXHgBQu5Q")
    print(response.content)
else :
    print "wrong input"
