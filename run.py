from bottle import Bottle, run
app = Bottle()

@app.route('/')
@app.route('/hello')
def hello_world():
        return "Hello World!"

run(app, host='127.0.0.1', port=8000, debug=True)
