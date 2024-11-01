import urllib.request as request
import os
import sys

'''
Airbnb Madrid
El objetivo de este trabajo es comprobar si se está utilizando la plataforma Airbnb por parte de empresas, en lugar de particulares, para alquiler turístico en el centro de Madrid.

Link csv:
https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/madrid-airbnb-listings-small.csv

Requisitos obligatorios
Sin usar Pandas:

1.Extraer del fichero de alojamientos una lista con todos los alojamientos, donde cada alojamiento sea un diccionario que contenga el identificador del alojamiento, el identificador del anfitrión, el distrito, el precio y las plazas.
2.Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.
3.Crear una función que reciba la lista de alojamientos y un número de ocupantes y devuelva la lista de alojamientos con un número de plazas mayor o igual que el número de ocupantes.
4.Crear una función que reciba la lista de alojamientos un distrito, y devuelva los 10 alojamientos más baratos del distrito.
5.Crear una función que reciba la lista de alojamientos y devuelva un diccionario con los anfitriones y el número de alojamientos que posee cada uno.

'''


'''
1.Extraer del fichero de alojamientos una lista con todos los alojamientos, donde cada alojamiento sea un diccionario que contenga:
identificador del alojamiento
identificador del anfitrión
distrito
precio
plazas
'''

def load_csv_file(url: str, local_path: str):
    try:
        response = request.urlopen(url)
        data = response.read().decode('utf-8')
        return data.splitlines()
    except Exception as e:
        print(f"Error al cargar desde la URL: {e}. \nCargando archivo local.")
        # Si hay un error, intenta cargar el archivo local
        if os.path.exists(local_path):
            with open(local_path, 'r', encoding='utf-8') as local_file:
                return local_file.readlines()  # Devuelve las líneas del archivo local
        else:
            print("El archivo local no existe.")
            return None


def extract_accommodation_info(csv_lines) -> list:
    accommodation_list = []

    for line in csv_lines[1:]:
        data = line.split("\t")
        
        info_hotel = {
            "id" : data[0],  # id del alojamiento
            "anfitrion" : data[19], # id del anfitrión
            "distrito" : data[40],
            "plazas" : data[53],  # capacidad
            "precio" : data[60]
        }

        accommodation_list.append(info_hotel)
    
    return accommodation_list


url = "https://aprendeconalf.es/docencia/python/trabajos/inteligencia-negocios/datos/madrid-airbnb-listings-small.csv"
local_file = "../../data/madrid-airbnb-listings-small.csv"

# Cargar el archivo desde la URL o localmente
csv_lines = load_csv_file(url, local_file)

if csv_lines:
    # Extraer la información de los alojamientos
    accommodations_list = extract_accommodation_info(csv_lines)
    print("Información de alojamientos extraída con éxito desde archivo local.")
else:
    print("No se pudo cargar el archivo.")
    sys.exit()

#print(accommodations_list)



'''
2.Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.
'''
def accommodations_per_district(accommodations_list: list) -> dict:
    dict_district = {}

    for i in accommodations_list:
        # Incrementa el conteo de alojamientos para el distrito actual.
        # Si el distrito ya está en el diccionario, se suma 1; 
        # si no, se inicializa en 0 y luego se suma 1.
        dict_district[i["distrito"]] = dict_district.get(i["distrito"], 0) +1
    
    return dict_district

#print(accommodations_per_district(accommodations_list))



'''
3.Crear una función que reciba la lista de alojamientos y un número de ocupantes y devuelva la lista de alojamientos con un número de plazas mayor o igual que el número de ocupantes.
'''

def filter_accommodations_by_capacity(accommodations_list: list, accommodates: int) -> list:
    return [x for x in accommodations_list if int(x["plazas"]) >= accommodates]

#print(filter_accommodations_by_capacity(accommodations_list, 10))



'''
4.Crear una función que reciba la lista de alojamientos un distrito, y devuelva los 10 alojamientos más baratos del distrito.
'''

def get_cheapest_accommodations_by_district(accommodations: list, district: str) -> list:
    accommodations_by_district = [x for x in accommodations if x["distrito"] == district]

     #Convierte el precio a float, omitiendo el símbolo $
    def sort_by_price(dict): 
        return float(dict["precio"][1:])

    cheapest_accommodations = sorted(accommodations_by_district, key= sort_by_price)

    return cheapest_accommodations[:10]

#print(get_cheapest_accommodations_by_district(accommodations_list, 'Arganzuela'))



'''
5.Crear una función que reciba la lista de alojamientos y devuelva un diccionario con los anfitriones y el número de alojamientos que posee cada uno.
'''

def count_accommodations_per_host(accommodations: list) -> dict:
    host_dict = {}
    for accommodation in accommodations:
        # Si el anfitrión ya está en el diccionario, se suma 1; de lo contrario, se inicializa en 0
        host_dict[accommodation["anfitrion"]] = host_dict.get(accommodation["anfitrion"], 0) + 1

    return host_dict

#print(count_accommodations_per_host(accommodations_list))