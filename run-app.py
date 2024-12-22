from app import app
import webbrowser
import os

if __name__ == '__main__':
  if os.environ.get("WERKZEUG_RUN_MAIN") is None:
    webbrowser.open('http://127.0.0.1:5000', new=0)
  app.run(debug=True)

