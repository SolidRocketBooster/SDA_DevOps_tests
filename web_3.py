import requests
nasa_page = 'https://api.nasa.gov/planetary/apod?api_key=2WXYt1ROSNekbcvxBBGJeOQ4mn6axkcqqqCCjD1E'
data_nasa = requests.get(nasa_page).json()
print(data_nasa['explanation'])
