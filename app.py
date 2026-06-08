

from datetime import date

from flask import Flask, Response, render_template, send_from_directory, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

SITE_URL = 'https://cgew.onrender.com'
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

# ================= SEO =================

@app.route('/robots.txt')
def robots():
    body = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""
    return Response(body, mimetype='text/plain')


@app.route('/sitemap.xml')
def sitemap():
    pages = [
        ('home', '1.0'),
        ('subjects', '0.9'),
        ('general_awareness', '0.9'),
        ('current_affairs', '0.8'),
    ]
    today = date.today().isoformat()
    urls = '\n'.join(
        f"""  <url>
    <loc>{SITE_URL}{url_for(endpoint)}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>"""
        for endpoint, priority in pages
    )
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    return Response(body, mimetype='application/xml')

# ================= ASSETS =================

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename, max_age=31536000)

# ================= RUN APP =================

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
