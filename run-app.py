from app import app
from livereload import Server
import webbrowser

host = '127.0.0.1'
port = '5500'

if __name__ == '__main__':
  app.config["TEMPLATES_AUTO_RELOAD"] = True

  server = Server(app.wsgi_app)

  server.watch('.\\app\\*.py')
  server.watch('.\\app\\static\\*\\*.*')
  server.watch('.\\app\\templates\\*.html')

  webbrowser.open(f'http://{host}:{port}')

  server.serve(port=port, host=host, debug=True)
