import os
import uuid
import cherrypy


if not os.path.exists("./api.key"):
    with open("./api.key", "w") as api_key_file:
        api_key_file.write(str(uuid.uuid4()))


with open("./api.key", "r") as api_key_file:
    API_KEY = api_key_file.read().rstrip("\n")


cherrypy.log("Using API KEY {0} for authentication".format(API_KEY))


def check_authentication():
    provided_key = cherrypy.request.headers.get("X-HTTP-APIKEY", None)
    cherrypy.log("API Key Provided by user was {0}".format(provided_key))
    if not provided_key == API_KEY:
        cherrypy.log("Raising 401 error as API key does not match expected")
        raise cherrypy.HTTPError(status=401, message="API Key Invalid")


cherrypy.tools.require_api_key = cherrypy.Tool("before_handler", check_authentication, priority=50)
