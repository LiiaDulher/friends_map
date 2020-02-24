from flask import Flask, render_template, request
import friends_map


app = Flask(__name__)


@app.route("/")
def user_map():
    return render_template(friends_map.create_map('', 'templates/'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
