from flask import Flask, request
from caeser import rotate_string

app = Flask(__name__)
app.config['Debug'] = True


page_header= """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form = {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>    
    <body>
"""

form = """ 
      <form method="post">
        <div>
        <label for "rot">
        Rotate by:
            <input name ="rot" type="text" value=0 />
        </label>
        </div>
        <textarea name= "text">{0}</textarea>
        <input type="submit"></input>
       </form>
    </body>
</html>
"""



@app.route("/", methods=['POST']) 
def encrypt():
    rotate_number = request.form['rot']
    string = request.form['text']
    message = rotate_string(string, rotate_number)
    return "<h1>" + message + "</h1>"


@app.route("/")
def index():
    return form


app.run()