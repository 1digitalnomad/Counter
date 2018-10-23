from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'CounterSecrets'

@app.route('/')
def index():
    try:
        session['counter']+=1
    except KeyError:
        session['counter']=1
    return render_template('index.html', counter=session['counter'])

@app.route('/uptwo')
def uptwo():
    session['counter']+=1
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)

