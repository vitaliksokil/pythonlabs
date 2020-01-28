import cgi
import math

form = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="post">
    <label for="AB"> AB </label>
        <input type="number" id="AB" name="AB">
    <label for="BC"> BC </label>
        <input type="number" id="BC" name="BC">
    <label for="CA"> CA </label>
        <input type="number" id="CA" name="CA">
    <button type="submit">Submit</button>
</form>
</body>
</html>
'''


def app(environ, start_response):
    html = form

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        AB = int(post['AB'].value)
        BC = int(post['BC'].value)
        CA = int(post['CA'].value)
        p = (AB + BC + CA) / 2
        S = math.sqrt(p * (p - AB) * (p - BC) * (p - CA))
        html = '''
            <h3> Triangle area: ''' + str(S) + ''' </h3>
        '''

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf8')]


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
