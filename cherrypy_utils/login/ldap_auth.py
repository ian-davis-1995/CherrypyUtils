# noinspection PyUnresolvedReferences, PyPackageRequirements
import ldap
import cherrypy

server_address = "ldap://srv-1:3899"
server = ldap.initialize(server_address)


def ldap_login(username, password):
    try:
        user = "uid={0}".format(username)
        cherrypy.log("Logging into LDAP server with credentials {0}".format(user))
        server.simple_bind_s(user, password)
        cherrypy.log("Login succeeded")
        return True
    except ldap.INVALID_CREDENTIALS:
        cherrypy.log("Login failed")
        return False
