from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']
        translation = translator.translate(text, dest=target_lang)
        return render_template('index.html', translation=translation.text)
    return render_template('index.html', translation=None)

if __name__ == '__main__':
    app.run(debug=True)