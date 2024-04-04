from dash import Dash, html, register_page, page_registry
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.CYBORG]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Initialise the app using bootstrap css
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags, use_pages=True, suppress_callback_exceptions=True)

# From https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Event Details", href=page_registry['pages.events']['path'])),
        dbc.NavItem(dbc.NavLink("Charts", href=page_registry['pages.charts']['path']))
    ],
    brand="Paralympics Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

page_container = html.Div([
    html.H2(["Paralypic Weekly Coding Activities"])
])

app.layout = html.Div([
    # Nav bar
    navbar,
    # Area where the page content is displayed
    page_container
])

if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
