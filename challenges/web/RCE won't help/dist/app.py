from flask import Flask, render_template_string, request, redirect, make_response
import os

app = Flask(__name__)
flag = "greyhats{redacted}"

# even rce cannot reverse this
with open("app.py","r") as f:
    file = f.read()
    file = file.replace(flag,"greyhats{redacted}")
with open("app.py","w") as f:
    f.write(file)

login_html = """
<form method="post" action="/login">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <br><br>
    <input type="submit" value="Login">
</form>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        response = make_response(redirect('/'))
        response.set_cookie('username', username)
        return response
    return login_html

@app.route('/')
def home():
    username = request.cookies.get('username')
    if username:
        print(username)
        return render_template_string(f"""Welcome {username}!""")
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
