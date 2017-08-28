import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['m1', 'm2', 'chi_p', 'chi_eff, 'Mc', 'Distance', 'q', 'spin1'],
    y=[8.322, 16.185, 5.2, 5.607, 29.673, 28.070, 50],
    name='Control',
    error_y=dict(
        type='data',
        array=[2.06, 33.83, 42, 29.673, 10.837, 58.596, 82.8],
        visible=True
)
trace2 = go.Bar(
    x=['m1', 'm2', 'chi_p', 'chi_eff, 'Mc', 'Distance', 'q', 'spin1'],
    y=[10.29, 23.73, 73.2, 18.457, 6.855, 38.947, 55.6],
    name='Experimental',
    error_y=dict(
        type='data',
        array=[2.00, 38.27, 54.6, 38.551, 11.751, 67.017, 79],
        visible=True
    )
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='error-bar-bar')
plt.savefig("Run14_test")
