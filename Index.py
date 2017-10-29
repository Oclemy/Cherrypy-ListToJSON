




# Import cherrypy and json
# Create a function that dumps or prints our list into json
import cherrypy
import json
class Index(object):

    @cherrypy.expose()
    def index(self):
        galaxies=["Messier 81","StarBurst","Black Eye","Cosmos Redshift","Sombrero","Hoags Object","Andromeda","Centarus A","Whirlpool","Canis Major Overdensity"]
        return json.dumps(galaxies)

if __name__ == '__main__':
       cherrypy.quickstart(Index())