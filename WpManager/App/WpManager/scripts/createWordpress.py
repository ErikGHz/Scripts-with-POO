import subprocess, shutil

class Wordpress:
    def __init__(self, titulo, usuario, contrasena, correo):
        self.titulo = titulo
        self.usuario = usuario
        self.contrasena = contrasena
        self.correo = correo

    def crearDirectorio(self):
        nombre_directorio = self.titulo
        sh_comando = f"sh crearWordpress.sh crear_directorio {nombre_directorio}"
        subprocess.run(sh_comando, shell=True)

    def copiarDocker(self):
        nombre_directorio = self.titulo
        sh_comando = f"sh crearWordpress.sh copiar_docker {nombre_directorio}"
        subprocess.run(sh_comando, shell=True)

    def 

nuevo_wordpress = Wordpress("Medicina", "", "", "")
nuevo_wordpress.crearDirectorio()
nuevo_wordpress.copiarDocker()
