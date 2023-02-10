import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("AtlaCV_Template.pdf")


app.run()

