import dash
import dash_table
import dash_html_components as html
import pandas as pd

df = pd.DataFrame(
    [
        ["California", 289, 4395, 15.3, 10826],
        ["Arizona", 48, 1078, 22.5, 2550],
        ["Nevada", 11, 238, 21.6, 557],
        ["New Mexico", 33, 261, 7.9, 590],
        ["Colorado", 20, 118, 5.9, 235],
    ],
    columns=["State", "# Solar Plants", "MW", "Mean MW/Plant", "GWh"],
)

app = dash.Dash(__name__)
server = app.server

app.layout = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("records"),
    export_format="csv",
)

if __name__ == "__main__":
    app.run_server(debug=True)