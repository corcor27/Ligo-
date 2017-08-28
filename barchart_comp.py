import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['m1', 'm2', 'chi_p', 'chi_eff, 'Mc', 'Distance', 'q', 'spin1', 'spin2'],
    y=[3, 6, 4],
    name='Control',
    error_y=dict(
        type='data',
        array=[0.5, 1, 2],
        visible=True
)
trace2 = go.Bar(
    x=['m1', 'm2', 'chi_p', 'chi_eff, 'Mc', 'Distance', 'q', 'spin1', 'spin2'],
    y=[4, 7, 3],
    name='Experimental',
    error_y=dict(
        type='data',
        array=[0.5, 1, 2],
        visible=True
    )
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='error-bar-bar')
