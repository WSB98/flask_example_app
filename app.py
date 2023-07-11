from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

#flask request and response handling
app = Flask(__name__, template_folder='templates')
CORS(app) #enable Cross Origin Resource Sharing (CORS)

# this opens up the landing page of the app
# navigation can be handled the way it usually is with JS or HTML
#   anchor tags // but there are cases where rendering a new page 
#   would be better
@app.route("/")
def index():
    return render_template('index.html')

# the following method shows a request that does not send any data
#   and returns data back to the request as a JSON
# this kind of request can be used to load data on boot
# if there are things that need to be loaded from the backend
# within the interface
@app.route("/basic-request", methods=['GET','POST'])
def basic_request():
    if(request.method == "POST"):
        # any data you want to return
        data = 'Success!'

        # format into a dictionary
        data = {'message': data}

        #jsonify the data to be returned
        return jsonify(data)
    
    # bad request response
    return 'method not allowed', 405

# this method shows a request coming in and being manipulated
#   then being returned back to the request in the form of a JSON
# this is how most buttons would function. send data from the frontend
#   and process it in some way, then return the results back to the fontend
#   everything else is handled with JS and CSS that manipulate the HTML
@app.route("/average-request", methods=['GET','POST'])
def average_request():

    # the if statement is the control of inflow / isnt necessary, but people do it for some reason
    if(request.method == "POST"):
        # get the data sent into the request
        data = request.json

        # do something with the data
        def doSomething(data):
            return {'message': "you sent " + data}

        # format into a dictionary
        manipulatedData = doSomething(data)

        # jsonify the returned data
        return jsonify(manipulatedData)
    
    # bad request response
    return 'method not allowed', 405

# host the app
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="80")