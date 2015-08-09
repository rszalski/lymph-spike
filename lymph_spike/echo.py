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
