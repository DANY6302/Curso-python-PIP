import csv #importa biblioteca csv
import utils

def read_csv(path):
  with open(path, 'r') as csvfile: #abre el archivo csv en modo lectura, la funcion with garantiza que el archivo se cierre correctamente despues de su uso
    reader = csv.reader(csvfile, delimiter=',') #crea un lector CSV iterable
    header = next(reader) #lee la primera linea del archivo saltandolo, por ende la iteracion comenzará en la segunda fila
    data = []
    for row in reader:
      iterable = zip(header, row) #Fusiona el header con el row convirtiendolo en un array de     tupplas
      country_dict = {key: value for key, value in iterable} #Crea un diccionario con el header y el row
      data.append(country_dict)
  return data

'''
def select_county(country):
  selected = list(filter(lambda item: item['Country/Territory'] == country, data))
  populations = utils.get_population(selected)
  return populations
'''

if __name__ == '__main__':
  data = read_csv('./app/data.csv')