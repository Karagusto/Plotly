import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ["http://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="Montréal"),
    dcc.Input(id="input-2", type="text", value="Canada"),
    dcc.Input(id="input-3", type="text", value="Maceió"),
    dcc.Input(id="input-4", type="text", value="Teste"),
    html.Div(id="number-output")
])

@app.callback(
    Output("number-output", "children"),
    [Input("input-1", "value"), Input("input-2", "value"), Input("input-3", "value"), Input("input-4", "value")],

)
def update_output(input1, input2, input3, input4):
    return u'Input 1 is "{}" and Input 2 is "{}" and Input 3 is "{}"'.format(input1, input2, input3, input4)


if __name__ == "__main__":
    app.run_server(debug=True)






























