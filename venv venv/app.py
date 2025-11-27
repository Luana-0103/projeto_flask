from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Olá, lask está funcionando!'

if _name_ == '_main_':
    app.run(debug=True)