from flask import Flask, render_template, request

app = Flask(__name__)


# Create a URL route in our application for "/"
@app.route("/", methods=['GET', 'POST'])
def chat_vfx():
    if request.method == 'POST':
        question = request.form.get('question', '')
        from chatBot.get_answer import get_answer
        answer = get_answer(question)
    else:
        answer = ''
    return render_template('index.html', answer=answer)


@app.route("/Documentation", methods=['GET', 'POST'])
def documentation():
    return render_template('Kitbash.html')


@app.route("/train_model", methods=['GET', 'POST'])
def train_model():
    from chatBot.create_embeddings import train_model
    train_model()
    return render_template('index.html')


# Run the app :)
if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
