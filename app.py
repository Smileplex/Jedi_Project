from flask import Flask, render_template
import os
import controllers 
app = Flask(__name__,  template_folder='views')


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
  #listen on external IPs
  print(os.getcwd())
  app.run(host='0.0.0.0', port=5710,debug=True)
