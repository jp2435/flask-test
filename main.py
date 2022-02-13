import os
from flask import Flask, redirect, url_for
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'Sweet home alabama'

@app.route('/alabama')
def alabama():
  return redirect('/never')
  #return 'Again Sweet home alabama'

@app.route('/never')
def sweet():
  rick()
  return 'never gonna give u up'

def rick():
  print('never gonna let u down')
'''
def run():
  app.run(host='0.0.0.0',port=8080)

def web_server():
    t = Thread(target=run)
    t.start()
'''

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
