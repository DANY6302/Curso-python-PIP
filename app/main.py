import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  labels, values = utils.get_world_percentages(data)
  charts.generate_pie_chart(labels, values)

  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0] #Lista de diccionarios
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

#Indica que si se ejecuta desde la terminal, se ejecute la funcion run()
if __name__ == '__main__': 
  run()