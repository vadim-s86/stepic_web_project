from cgi import parse_qsl, escape
def wsgi_application(environ, start_response):

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    pars = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            for ch in d:
                data.append(' = '.join(ch))
                data.append('<br>')
    start_response(status, headers)
    return data
