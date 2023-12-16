from flask import Flask

app = Flask(__name__)

@app.route('/division/<int:num1>/<int:num2>', methods=['GET'])
def division(num1=None, num2=None):
    
    if num1 is None or num2 is None:
        return "Absence de 'num1' ou 'num2'"
    
    if num2 == 0:
        return "Deuxeme chiffre ne doit pas etre 0"
    
    result = num1 / num2
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
