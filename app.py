from flask import Flask, render_template, request


app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route("/", methods=['GET', 'POST'])
def chat_vfx():
    if request.method == 'POST':
        question = request.form.get('question', '')
        import chatBot
        answer = chatBot.get_answer(question)
    else:
        answer = ''
    return render_template('index.html', answer=answer)

# Run the app :)
if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
