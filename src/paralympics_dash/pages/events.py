from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import register_page, get_asset_url, page_registry

register_page(__name__, name='Events', title='Events', path="/")

row_one = dbc.Row([
    dbc.Col(children=[
        html.H1("Paralympics Data Analytics"),
        html.P(
            "Some stuff about events."
        )
    ])
])

row_three = dbc.Row([
    dbc.Col(children=[

        # Column 1 children
        html.Img(src=get_asset_url('map-placeholder.png'), className="img-fluid"),

        # Column 2 children
        dbc.Card(
            [
                dbc.CardImg(src="assets/logos/1960_Rome.png", top=True),
                dbc.CardBody(
                    [
                        html.H4("TownName 2026", className="card-title"),
                        html.P(
                            "Highlights of the paralympic event will go here. This will be a sentence or two.",
                            className="card-text",
                        ),
                        html.P(
                            "Number of athletes: XX",
                            className="card-text",
                        ),
                        html.P(
                            "Number of events: XX",
                            className="card-text",
                        ),
                        html.P(
                            "Number of countries: XX",
                            className="card-text",
                        )
                    ]
                )
            ]
            # style={"width": "18rem"},
        )
    ], width=6),
    dbc.Col(children=[], width=6),
])

layout = dbc.Container([
    row_one,
    row_three
])