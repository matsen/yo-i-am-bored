#!/usr/bin/env python

import datetime
import sys
from twisted.web import server, resource
from twisted.internet import reactor, endpoints

default_port = 8080
# How long yos take to expire.
expiration_time = datetime.timedelta(minutes=5)
# Page auto refresh time in seconds.
refresh_period = 10

yos = dict()


def cull_yos():
    now = datetime.datetime.now()
    for (k, v) in yos.items():
        if now - v > expiration_time:
            yos.pop(k)


class Counter(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        cull_yos()
        if 'username' in request.args:
            name = request.args['username'][0]
            yos[name] = datetime.datetime.now()
        request.setHeader('refresh', str(refresh_period))
        return 'bored: ' + ', '.join(yos.keys()) + '\n'


if __name__ == '__main__':
    port = default_port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    print "Listening for boredom on http://localhost:{}/".format(port)
    s = endpoints.serverFromString(reactor, 'tcp:'+str(port))
    s.listen(server.Site(Counter()))
    reactor.run()
