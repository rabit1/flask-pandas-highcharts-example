from flask import Flask, render_template, request
import pandas as pd
import pandas_highcharts.core

app = Flask(__name__)

@app.route('/graph')
def graph_Example(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
#    df = pd.read_csv('csv/BCHAIN-TRVOU-BitcoinUSDExchangeTradeVolume.csv', index_col='Date', parse_dates=True)
    df = pd.read_csv('csv/test.csv', index_col='Date', parse_dates=True)
    dataSet = pandas_highcharts.core.serialize(df, render_to='my-chart', output_type='json')
    return render_template('graph.html', chart=dataSet)

@app.route('/')
def main():
	return "Hi"

app.run(debug=True)

