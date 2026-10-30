
from flask import Flask, render_template, request

app = Flask(__name__)

# Список для зберігання зареєстрованих користувачів
users = []


# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')


# Сторінка реєстрації
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        users.append({
            'name': name,
            'email': email,
            'message': message
        })

        return render_template(
            'result.html',
            name=name,
            email=email,
            message=message
        )

    return render_template('register.html')


# Сторінка зі списком користувачів
@app.route('/users')
def show_users():
    return render_template('users.html', users=users)
    
# Сторінка галереї
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
