# all the imports
import logging
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from BT4221 import *

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/livedemo', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        logging.info("POST")
        day = int(request.form["Day"])
        month = int(request.form["Month"])
        region =  int(request.form["Region"])
        properties = int(request.form["Property"])
        extproperties = int(request.form["extproperty"])
        specificity = int( request.form["spec"])
        att = int( request.form["att"])
        weapon = int( request.form["weapon"])
        prep = int( request.form["numprep"])
        

        res= lm.predict([month, day,region,properties,extproperties,att,weapon,prep,specificity])
        res_rf= forest.predict_proba([month, day,region,properties,extproperties,att,weapon,prep,specificity])
        res_lr= model2.predict_proba([month, day,region,properties,extproperties,att,weapon,prep,specificity])
        counter= plots(res,res_rf,res_lr)
        return render_template('pages/livedemo.html', result=res[0], lr =res_lr[0][1], rf=res_rf[0][0], plot=counter)
    logging.info("GET")
    return render_template('pages/livedemo.html', result=None, lr =None, rf=None)

@app.route('/dataset')
def dataset():
    return render_template('pages/dataset.html')

@app.route('/regression')
def regression():
    return render_template('pages/regression.html')

@app.route('/randomforest')
def randomforest():
    return render_template('pages/randomforest.html')
@app.route('/marketbasket')
def marketbasket():
    return render_template('pages/marketbasket.html')

@app.route('/prelim')
def prelim():
    #maps_plot = maps()
    return render_template('pages/prelim.html')
if __name__ == "__main__":
    app.run(debug=True)
