#!/usr/bin/env python3
#Author: Hans Saldias

from PIL import Image
import os
import sys # Importar sys para salir del script si la respuesta es 'no'

print("Script para comprimir peso de imagenes")
print("Ejecuta el script donde tengas todas las imagenes para comprimirlas")
print("Script creado por Hans Saldias\n")

op = input("Aceptas comprimir las imagenes (si/no): ").lower() # Convertir a minúsculas para una mejor comparación
print("\n")

if op == "si":
    # 1. Crear la carpeta si no existe
    directorio_salida = 'imagenes_comprimidas'
    if not os.path.exists(directorio_salida):
        os.mkdir(directorio_salida)

    imagenes_comprimidas_count = 0
    
    # 2. Definir las extensiones de imagen que queremos procesar (en minúsculas y mayúsculas)
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    
    # 3. Iterar sobre todos los archivos
    for imagen in os.listdir('.'):
        
        # OMITIR: Si es .mp4, lo saltamos y vamos al siguiente archivo (CONTINUE)
        if imagen.endswith('.mp4'):
            print(f"Saltando archivo de video: {imagen}")
            continue
            
        # OMITIR: Si es el directorio de salida, también lo saltamos
        if imagen == directorio_salida:
            continue

        # PROCESAR: Si tiene una de las extensiones de imagen válidas
        if imagen.endswith(extensiones_validas):
            try:
                # Extraer el nombre del archivo sin la extensión
                nombre = os.path.splitext(imagen)[0]

                # Abrir la imagen
                img = Image.open(imagen)

                # Guardar la imagen comprimida. Se guarda como JPG por defecto con calidad 50.
                ruta_salida = os.path.join(directorio_salida, f'{nombre}.jpg')
                img.save(ruta_salida, optimize=True, quality=50)
                
                print(f"Compresión exitosa: {imagen} -> {ruta_salida}")
                imagenes_comprimidas_count += 1
                
            except FileNotFoundError:
                print(f"Error: No se pudo encontrar el archivo {imagen}")
            except Exception as e:
                print(f"Error al procesar {imagen}: {e}")

    # 4. Mensaje de finalización
    print("#" * 60)
    if imagenes_comprimidas_count > 0:
        print(f"¡Proceso finalizado! {imagenes_comprimidas_count} imágenes han sido guardadas")
        print(f"exitosamente en la carpeta '{directorio_salida}'")
    else:
        print("No se encontraron imágenes para comprimir (archivos .jpg, .png, .jpeg)")
    print("#" * 60)

else:
    print("Operación cancelada. Saliendo del script.")
    sys.exit() # Salir del script si el usuario dice 'no'

print("Creador: Hans Saldias")
