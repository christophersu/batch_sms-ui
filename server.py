from flask import Flask

from basic_auth import requires_auth
import batch_sms

app = Flask(__name__)

@app.route('/')
@requires_auth
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)