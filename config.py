# Nombre del módulo: config

import os

# Nombres de las variables globales
_global_vars = ['modo', 'safegraphic', 'debug']

# Valores por defecto de las variables
_default_vals = {'modo': 0, 'safegraphic': 0, 'debug': 0}

# Ruta del archivo de configuración
_config_file = 'config.txt'


def read_config():
    # Comprobar si el archivo de configuración existe
    if os.path.isfile(_config_file):
        with open(_config_file, 'r') as f:
            # Leer las líneas del archivo y eliminar los espacios en blanco
            lines = [line.strip() for line in f.readlines()]
            # Crear un diccionario con las variables globales y sus valores
            global_vars_dict = dict(zip(_global_vars, lines))
            # Convertir los valores a los tipos de datos apropiados
            for key, value in global_vars_dict.items():
                if value.isdigit():
                    global_vars_dict[key] = int(value)
                elif value.lower() in ['true', 'false']:
                    global_vars_dict[key] = value.lower() == 'true'
            # Actualizar las variables globales con los valores leídos del archivo
            globals().update(global_vars_dict)
    else:
        # Si el archivo no existe, establecer los valores por defecto
        globals().update(_default_vals)
        write_config()  # Crear el archivo de configuración


def write_config():
    with open(_config_file, 'w') as f:
        # Escribir las variables globales en el archivo
        for var in _global_vars:
            f.write(str(globals()[var]) + '\n')


# Llamada a la función para leer las variables de configuración
read_config()
