from flask import Flask, request, redirect, render_template
import cgi
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True      


@app.route("/validate", methods=['POST'])
def add_info():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form ['verify_password']
    email = request.form ['email']

    # identify types of errors

    if (not username) or (username.strip() == ""):
        username_error_1 = "Please add a username."
        return render_template('home.html', username=username, email=email, 
        username_error_1=username_error_1)

    if " " in (username.strip()):
        username_error_2 = "Spaces not allowed, please enter a new username."
        return render_template('home.html', username=username, email=email, 
        username_error_2=username_error_2)

    if len(username) < 3:
        username_error_3 = "Username must be at least 3 characters long."
        return render_template('home.html', username=username, email=email,
        username_error_3=username_error_3)

    if len(username) > 20:
        username_error_4 = "Please enter a username shorter than 20 characters long."
        return render_template('home.html', username=username, email=email,
        username_error_4=username_error_4)

    if (not password) or (password.strip() == ""):
        password_error_1 = "Please add a password."
        return render_template('home.html', username=username, email=email,
        password_error_1=password_error_1)

    if " " in (password.strip()):
        password_error_3 = "Spaces not allowed, please enter a new password."
        return render_template('home.html', username=username, email=email,
        password_error_3=password_error_3)

    if len(password) < 3:
        password_error_4 = "Password must be at least 3 characters long."
        return render_template('home.html', username=username, email=email,
        password_error_4=password_error_4)

    if len(password) > 20:
        password_error_5 = "Please enter a password shorter than 20 characters long."
        return render_template('home.html', username=username, email=email, 
        password_error_5=password_error_5)

    if (not verify_password) or (verify_password.strip() == ""):
        verify_error_1 = "Please verify your password."
        return render_template('home.html', username=username, email=email,
        verify_error_1=verify_error_1)

    if (password) != (verify_password):
        verify_error_2 = "Passwords didn't match, please try again."
        return render_template('home.html', username=username, email=email,
        verify_error_2=verify_error_2)

    if (email) and "@" not in (email.strip()): 
        email_error_1 = "Please enter a valid email address."
        return render_template('home.html', username=username, email=email, 
        email_error_1=email_error_1)

    if (email) and "." not in (email.strip()):
        email_error_2 = "Please enter a valid email address."
        return render_template('home.html', username=username, email=email, 
        email_error_2=email_error_2)

    if len(email) < 3: 
        email_error_3 = "Please enter a valid email address."
        return render_template('home.html', username=username, email=email, 
        email_error_3=email_error_3)

    if len(email) > 20:
        email_error_4 = "Please enter a shorter email address."
        return render_template('home.html', username=username, email=email, 
        email_error_4=email_error_4)

    if (email) and " " in (email.strip()):
        email_error_5 = "Spaces not allowed, please try again."
        return render_template('home.html', username=username, email=email, 
        email_error_5=email_error_5)

    # create escaped variables
    username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verify_password_escaped = cgi.escape(verify_password, quote=True)
    email_escaped = cgi.escape(email, quote=True)

    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('home.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
