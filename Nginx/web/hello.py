
'''
    Wsgi application
    <environ> is kwarg variables of environment
    <start_request> is function for send status_code and headers
'''
def wsgi_application(environ, start_request):
   # start_request("200 OK", [("Content-Type", "text/plain")])
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body
