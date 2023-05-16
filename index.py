from app import app, server  # Import the Dash app and its server
from callbacks import register_callbacks  # Import function to add callbacks to the app

register_callbacks(app)  # Add callbacks to the app

# to start the server
if __name__ == "__main__":
    server.run(debug=True)

