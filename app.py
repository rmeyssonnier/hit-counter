from flask import Flask


class HitCounterApp:
    def __init__(self, name):
        self.counter = 0
        self.app = Flask(name)
        self.register_urls()

    def run(self):
        self.app.run(host='0.0.0.0', port=34001)

    def register_urls(self):
        self.app.add_url_rule('/', 'hit', self.hit)
        self.app.add_url_rule('/reset', 'reset', self.reset)

    def hit(self):
        self.counter += 1
        return 'Counter hit {} times'.format(self.counter)

    def reset(self):
        self.counter = 0
        return 'Counter reset'


if __name__ == '__main__':
    app = HitCounterApp('hitcounter')
    app.run()
