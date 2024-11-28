import requests

url = "https://api.themoviedb.org/3/account/21658183/lists?page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTgwZGY3M2I1NTEzOWViY2Y5YTA1M2RiZGFmNDAzMSIsIm5iZiI6MTczMjgxNzM3Ny4zNDU5Nzg3LCJzdWIiOiI2NzQ4YWZiMDJhNTYyMmIxMDU3MTg0Y2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.-JuNVRyIRWWkOfhI96_3xRmaoX0jSL-VRiwzTPPfch8"
}

response = requests.get(url, headers=headers)

print(response.text)