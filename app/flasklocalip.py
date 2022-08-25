"""
Create an app (web app) that prints the local IP to the browser (on HTTP - port 80) Use any coding language you want
"""

from flask import Flask
import socket

# Creating the instance of the class Flask
app = Flask(__name__)


# Using the decorator to create the URL for the web application
@app.route('/')
# The function will return the local Host IP, displayed on the webpage
def local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return '<h1> Your local Host IP Address is: ' + ip_address


# Run the application
if __name__ == '__main__':
    app.run(debug=True)

