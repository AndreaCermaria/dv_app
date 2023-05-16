from dash import Dash  # Import Dash class to create the web application
from layout import layout  # Import layout, which defines how your app will look like

app = Dash(__name__)  # Create an instance of Dash class
app.layout = layout  # Set the layout of the application

server = app.server  # Flask server for deploying the application

# Setting this to True allows dynamic updates to the layout without throwing exceptions
app.config.suppress_callback_exceptions = True

