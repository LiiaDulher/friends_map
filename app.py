from flask import Flask, render_template, request, flash, redirect
import friends_map
from forms import UserIdForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=['GET', "POST"])
def get_user_id():
    form = UserIdForm()
    if form.validate_on_submit():
        user_id = form.username.data
        print(user_id)
        result = friends_map.create_map(user_id, '/home/LiiaDulher/twitter/templates/')
        if result:
            with open('/home/LiiaDulher/twitter/templates/' + result) as file:
                return file.read()
    return render_template('user.html', title="Enter user's id", form=form)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
