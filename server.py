from flask import Flask, render_template

from basic_auth import requires_auth
import batch_sms

app = Flask(__name__)

@app.route('/')
@requires_auth
def index():
    temp = ['this', 'is a', 'subscriber', 'list']
    return render_template('main.html', subscriber_lists=temp)

if __name__ == '__main__':
    app.run(debug=True)