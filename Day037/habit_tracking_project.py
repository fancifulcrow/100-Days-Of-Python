import requests
from datetime import datetime

pixela_url = "https://pixe.la/v1/users"

USERNAME = "wxxxr23491"
TOKEN ="aqlskemfwomffoasddccc"
GRAPH_ID = "graph-running"

user_params = {
    "token":TOKEN, 
    "username":USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes",
}

# create a user in pixela
# response = requests.post(url=f"{pixela_url}", json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name":"Running",
    "unit":"km",
    "type":"float",
    "color":"kuro"
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# You can attach your API key to a request in one ofthree ways:
# - Via the API Key querystring parameter
# - Via X-API-KEY HTTP header
# - Via the Authorization HTTP header
# Option 2 and 3 are more secure

# Create a graph
# response = requests.post(url=f"{pixela_url}/{USERNAME}/graphs", json=graph_config, headers=headers)
# print(response.text)

# view graph at: https://pixe.la/v1/users/USERNAME/graphs/graph_id.html

today = datetime.now().strftime("%Y%m%d") # Format: YYYYMMDD

# Create a pixel
create_pixel = {
    "date" : today,
    "quantity" : "15",
}

# response = requests.post(url=f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}", json=create_pixel, headers=headers)
# print(response.text)

# Update a pixel
update_pixel = {
    "quantity" : "7.5",
}

# response = requests.put(url=f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{today}", json= update_pixel, headers=headers)
# print(response.text)

# Delete a pixel
# response = requests.delete(url=f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=headers)
# print(response.text)