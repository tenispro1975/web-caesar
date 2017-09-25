from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True


newform="""
<!DOCTYPE html>
<html>
    <head>
        <style>
           form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
  
        </style>
    </head>
    <body>
        <form method="POST">
            <div>
                <label for="rotate_by">Rotate By:</label>       
                <input type="text" id="rotate_by" name="rot" value="0"/>
            </div>
                <textarea name="text" required>{0}</textarea>
                <br>
                <input type="Submit"/>
                
        </form>
    </body>
</html>
"""
@app.route("/",  methods=['POST'])
def encrypt():

    rot = int(request.form['rot'])
    text = str(request.form['text'])
    
    new_message = ""
    message = rotate_string(text, rot)
    new_message = message
        

    return newform.format(new_message)

@app.route("/")
def index():
    return newform.format("")



app.run() 
