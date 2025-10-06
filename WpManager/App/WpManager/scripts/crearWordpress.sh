#!/bin/bash
#Variable proviene de crearWordpress.py


#Ruta donde se crearan los directorios de cada wordpress
cd ../wordpress

#Si no existe el directorio, crea uno con el nombre del wordpress
crear_directorio(){
    nombre_directorio="$1"
    if [ -d "$nombre_directorio" ]; 
    then
        echo "El directorio ya existe: $nombre_directorio"
    else
        mkdir "$nombre_directorio"
        echo "Directorio creado correctamente: $nombre_directorio"
    fi
}

#Si existe el directorio, copia los archivos necesarios para levantar un wordpress
copiar_docker(){
    nombre_directorio="$1"
    if [ -d "$nombre_directorio" ]; 
    then
        cp -r ./template/wordpress "$nombre_directorio"
        cp ./template/docker-compose.yaml "$nombre_directorio"
        cp ./template/.env "$nombre_directorio"
        echo "Docker copiado correctamente"
    else
        echo "El directorio ${nombre_directorio} no existe"
    fi
}

"$@"