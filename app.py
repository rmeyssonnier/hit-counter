from flask import Flask

counter = 0
app = Flask(__name__)


@app.route('/')
def hit():
    global counter
    counter += 1
    return 'Counter hit {} times'.format(counter)


@app.route('/reset')
def reset():
    global counter
    counter = 0
    return 'Counter reset'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34001)
