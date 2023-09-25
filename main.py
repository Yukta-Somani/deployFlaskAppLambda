import awsgi
from flask import(
    Flask,
    jsonify
)

app =Flask(__name__)

@app.route('/')
def index():
    return jsonify(status=200,message='OK')

@app.route('/version')
def get_version():
    return {"version": "the current verion is 1.0.0"}

@app.route('/profile')
def get_name():
    return {"name": "AWS DEV"}


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == "__main__":
    app.run()