from flask import Flask,render_template,request,redirect, Markup
import requests
import simplejson as json
from datetime import datetime
from bokeh.plotting import figure, show
from bokeh.embed import components
    

#from DI2_Finalist22_noroot.py


app = Flask(__name__)
app.vars={}


#def get_date(jsondate):
#    return int(jsondate[:4]), int(jsondate[5:7]), int(jsondate[8:])



@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo.html')
    else:
        #request was a POST
        app.vars['movie'] = request.form['movie_lulu']
       
        movie = app.vars['movie']
        print "Movie = ", movie

        app.vars['stars'] = request.form['stars_lulu']
        stars = app.vars['stars']
        print "Stars =", stars
        print "OKAYYYS"
        WhatRank = []
        WhatScore = []
        WhatMovie = []
        print "OKAYa"
        import DI2_Finalist22_noroot
        WhatRank, WhatScore, WhatMovie = AAMainCode("Toy Story (1995)", "3")
        #WhatRank, WhatScore, WhatMovie = AAMainCode(str(movie), str(stars))
        print "Okayb"
        print WhatRank[-1], WhatScore[-1], WhatMovie[-1]
        print WhatRank[-2], WhatScore[-2], WhatMovie[-2]
        print "OKAAAAY"

        return render_template("error.html")
        #path = 'https://www.quandl.com/api/v3/datasets/WIKI/%s.json' % (stock)

#        try:
#            r = requests.get(path)
#
#            thedict = json.loads(r.text)
#            newestdate = thedict["dataset"]["newest_available_date"]
#            newestyear, newestmonth, newestday = get_date(newestdate)
#            prioryear = newestyear
#            priormonth = newestmonth - 1
#            priorday = newestday
#            if priormonth == 0:
#                priormonth = 12
#                prioryear = prioryear - 1
#            priordate = '%s-%s-%s' % (prioryear, priormonth, priorday)
#            columnnames = thedict["dataset"]["column_names"]
#            datecol = columnnames.index("Date")
#            closecol = columnnames.index("Close")
#            adjclosecol = columnnames.index("Adj. Close")
#            volumecol = columnnames.index("Volume")
#            print newestdate, newestyear, newestmonth, newestday
#            print priordate, prioryear, priormonth, priorday
#            data = thedict["dataset"]["data"]
#
#
#            #range okay
#            p = figure(width=800, height=500, x_axis_type="datetime", x_range=(datetime(prioryear,priormonth,priorday), datetime(newestyear,newestmonth,newestday)))
#
#
#            datelist = []
#            closecollist = []
#            volumecollist = []
#            adjclosecollist = []
#            for row in data:
#                rowyear, rowmonth, rowday = get_date(row[datecol])
#                datelist.append(datetime(rowyear,rowmonth,rowday))
#                closecollist.append(row[closecol])
#                volumecollist.append(row[volumecol])
#                adjclosecollist.append(row[adjclosecol])
#
#            if app.vars['volume']=='checked':
#                p.line(datelist, volumecollist, color='red', alpha=0.5, legend='Volume')
#
#            if app.vars['aprice']=='checked':
#                p.line(datelist, adjclosecollist, color='green', alpha=0.5, legend='Adjusted closing price')
#
#            if app.vars['cprice']=='checked':
#                p.line(datelist, closecollist, color='navy', alpha=0.5, legend='Closing price')
#
#
#            p.title = "%s stock fluctuations for the last month" % (stock)
#            p.xaxis.axis_label = 'date'
#
#            script, div = components(p)
#            return render_template("graph.html", script=Markup(script),div=Markup(div))
#
#
#
#        except:
#            return render_template("error.html")





@app.route('/')
def redir():
    return redirect('/index')




if __name__ == "__main__":
    app.run()


