from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def Home():
  return '<h1>Oi Lads.</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

  