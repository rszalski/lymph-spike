from lymph.core.declarations import proxy
from lymph.web.interfaces import WebServiceInterface
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response


class Web(WebServiceInterface):
    url_map = Map([
        Rule('/greet', endpoint='greet')
    ])

    def greet(self, request):
        name = request.args['name']
        print('Greeting with web {}'.format(name))
        greeting = proxy('Echo').greet(name=name)
        return Response(greeting)
