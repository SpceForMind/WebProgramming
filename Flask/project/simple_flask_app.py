
from flask import Flask

'''
    Create wsgi-application
'''
app = Flask(__name__)

'''
    Routing
'''
@app.route(r'/hello/')
def hello():
    return 'It hello'

if __name__ == "__main__":
    '''
        Run server on host 0.0.0.0
    '''
    app.run(host = "0.0.0.0")
