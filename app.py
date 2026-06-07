

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')
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

# ================= GENERAL AWARENESS =================

@app.route('/gn')
def general_awareness():
    return render_template('gn.html')

# ================= CURRENT AFFAIRS =================

@app.route('/current-affairs')
def current_affairs():
    return render_template('current_affairs.html')

# ================= ASSETS =================

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

# ================= RUN APP =================

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
