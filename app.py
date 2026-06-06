from flask import Flask, render_template

app = Flask(__name__)

# ================= HOME =================

@app.route('/')
def home():
    return render_template('home.html')

# ================= SUBJECTS =================

@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

# ================= TOPIC PAGE =================

@app.route('/template-topic')
def template_topic():
    return render_template('topic.html')

# ================= RUN APP =================

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )