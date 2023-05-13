from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader as pdr
import plotly.graph_objs as go
from flask import Flask, render_template

app = Flask(__name__)

start_date = datetime.now() - relativedelta(years=1)
end_date = datetime.now()

df = pdr.get_data_yahoo('AAPL', start=start_date, end=end_date)

data = [
    go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        mode='lines',
        name='AAPL'
    )
]

layout = go.Layout(
    title='AAPL - Preço de fechamento ajustado',
    xaxis=dict(title='Data'),
    yaxis=dict(title='Preço de fechamento ajustado')
)

fig = go.Figure(data=data, layout=layout)

@app.route('/')
def index():
    return render_template('index.html', plot=fig.to_html())

if __name__ == '__main__':
    app.run(debug=True)