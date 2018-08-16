
'''
    Wsgi application
    <environ> is kwarg variables of environment
    <start_request> is function for send status_code and headers
    Using version of python -2.7(requier in stepik terminal)
'''
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = [bytes(i + '\n') for i in environ['QUERY_STRING'].split('&')]
    return body
