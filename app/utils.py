def get_population(data):
  population_dict = {
    '2022': int(data['2022 Population']),
    '2020': int(data['2020 Population']),
    '2015': int(data['2015 Population']),
    '2010': int(data['2010 Population']),
    '2000': int(data['2000 Population']),
    '1990': int(data['1990 Population']),
    '1980': int(data['1980 Population']),
    '1970': int(data['1970 Population'])
  }
  return population_dict.keys(), population_dict.values()

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_world_percentages(data):
  percentages_dict = {
    item['Country/Territory']: item['World Population Percentage'] for item in data
  }
  return percentages_dict.keys(), percentages_dict.values()