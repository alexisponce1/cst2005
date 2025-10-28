# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)


# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '<b>Hello world from Flask!<b> <p>Genevieve M. : afaik</p>'

# --app Practice --debug run 


@app.route('/welcome')
def wc():
   s1 = 'Welcome to my page! '
   s2 = 'Have a nice day!'
   return s1 + s2

@app.route('/alexis')
def t_test():
   return render_template('my_template_1.html')
