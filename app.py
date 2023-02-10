import flask

app = flask.Flask(__name__)

@app.route('/')
def resume():
    return flask.send_file("AltaCV_Template.pdf")


app.run()

