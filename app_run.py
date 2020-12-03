from main_app import app

# [RUN APP] ----------------------------------------------------------------------------------------------------
port_number = 5148  # Run the app from terminal 'python3 app.py', change port number iof already in use
if __name__ == "__main__":
    app.run(port=port_number)
# --------------------------------------------------------------------------------------------------------------