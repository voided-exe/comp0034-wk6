from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import register_page, get_asset_url, page_registry

register_page(__name__, name='Charts', title='Charts')

row_one = dbc.Row([
    dbc.Col(children=[
        html.H1("Paralympics Data Analytics"),
        html.P(
            "Some stuff about charts."
        )
    ])
])

row_two = dbc.Row([
    dbc.Col(children=[

        # Column 1 children
        dbc.Select(
            options=[
                {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",  # The default selection
            id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
        ),

        # Column 2 children
        # className="ing-fluid" is a pure Bootstrap class and prevented the image spanning the next column
        html.Img(src=get_asset_url('line-chart-placeholder.png'), className="img-fluid"),

        # Column 3 children
        html.Div(
            [
                dbc.Label("Select the Paralympic Games type"),
                dbc.Checklist(
                    options=[
                        {"label": "Summer", "value": "summer"},
                        {"label": "Winter", "value": "winter"},
                    ],
                    value=["summer"],  # Values is a list as you can select 1 AND 2
                    id="checklist-input",
                )
            ]
        ),

        # Column 4 children
        html.Img(src=get_asset_url('bar-chart-placeholder.png'), className="img-fluid")
    ])
])

layout = dbc.Container([
    row_one,
    row_two
])