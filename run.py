import bottle

from blog import myapp
import settings

bottle.debug(settings.DEBUG)

if settings.DEBUG:
	bottle.TEMPLATES.clear()

bottle.run(app=myapp, host='0.0.0.0', port='8080', reloader=False)#settings.DEBUG)