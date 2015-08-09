import lymph


class Echo(lymph.Interface):
    @lymph.rpc()
    def echo(self, text=None):
        return text

    @lymph.rpc()
    def greet(self, name):
        print('Saying Hi!')
        self.emit('greeted', {'result': 'Said hi!'})
        return 'Hi, {}!'.format(name)


class Listen(lymph.Interface):
    @lymph.event('greeted')
    def on_greeted(self, event):
        print('Someone {}!'.format(event['result']))
