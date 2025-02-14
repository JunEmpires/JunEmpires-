from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Juniorjunempires@gmail.com'
app.config['MAIL_PASSWORD'] = 'ton-mot-de-passe'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Envoi de l'email
    msg = Message('Nouveau message de contact', sender=email, recipients=['Juniorjunempires@gmail.com'])
    msg.body = f"Nom: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)