import requests
def get_categories():
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  print(r.status_code) #Status code 200, sdigifica OK
  print(r.text)
  print(type(r.text))
  categories = r.json()
  for category in categories:
    print(category['name'])