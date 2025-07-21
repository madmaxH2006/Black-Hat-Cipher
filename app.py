from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Calculate the shifted position
            shifted_pos = (ord(char) - start + shift) % 26
            result += chr(start + shifted_pos)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_text = ''
    if request.method == 'POST':
        message = request.form['message']
        try:
            shift = int(request.form['shift'])
            if 'encrypt' in request.form:
                processed_text = caesar_cipher(message, shift, 'encrypt')
            elif 'decrypt' in request.form:
                processed_text = caesar_cipher(message, shift, 'decrypt')
        except ValueError:
            processed_text = "ERROR: Shift key must be an integer."
            
    return render_template('index.html', processed_text=processed_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    