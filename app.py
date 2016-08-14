from flask import Flask, render_template, request, redirect
from retrieve_stock_data import retrieve_data, plot_data
import traceback

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    print "Arrived in main"
    return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
    print "Arrived in index"
    print "request.method: " + request.method
    
    if request.method == 'GET':
        print "Arrived in GET"
        return render_template('index.html',bokeh_script="",bokeh_div="",note="")
        
    else:
        print "Arrived in POST"
        # Try to retrieve the data
        try:
            print request.form['ticker']
            data = retrieve_data(request.form['ticker'])
            print data
        except:
            note = "ERROR getting stock data! Faulty ticker symbol?"
            return render_template('index.html',bokeh_script="",bokeh_div="",note=note)
        # Generate bokeh plot
        desired_columns = request.form.getlist('features')
        script,div,note = plot_data(data,desired_columns,request.form['ticker'])
        # Render plot
        return render_template('index.html',bokeh_script=script,bokeh_div=div,note=note)

if __name__ == '__main__':
    app.run(port=33507)
    #app.run(host='0.0.0.0')
