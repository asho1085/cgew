

from datetime import date

from flask import Flask, Response, redirect, render_template, send_from_directory, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000

SITE_URL = 'https://cgew.onrender.com'


@app.after_request
def add_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' https://cgew.onrender.com data:; "
        "base-uri 'self'; "
        "frame-ancestors 'none'; "
        "form-action 'self'"
    )
    return response
# ================= HOME =================

@app.route('/')
def home():
    return render_template('home.html')

# ================= SEARCH LANDING PAGES =================

SEO_PAGES = {
    'how-to-crack-government-exam': {
        'title': 'How to Crack Government Exam | CGE Preparation Guide',
        'description': 'Learn how to crack government exams with a practical study plan, subject-wise notes, revision strategy, and current affairs preparation from CGE.',
        'heading': 'How to Crack Government Exam',
        'intro': 'A clear government exam preparation plan helps you study the right subjects, revise consistently, and practice exam-style questions before the test.',
        'canonical': '/how-to-crack-government-exam',
        'sections': [
            ('Start with the syllabus', 'Read the official syllabus first, then divide topics into General Awareness, Reasoning, Mathematics, English, and exam-specific sections.'),
            ('Use short notes for revision', 'Keep concise notes for formulas, current affairs, static GK, important dates, and repeated question patterns.'),
            ('Practice every week', 'Solve previous year questions and mock tests regularly so speed, accuracy, and time management improve together.'),
        ],
        'faqs': [
            ('How can I crack a government exam?', 'Follow the syllabus, study one subject at a time, revise short notes, practice previous year questions, and take mock tests.'),
            ('Are notes useful for government exam preparation?', 'Yes. Good notes help you revise faster and remember high-value facts, formulas, and current affairs.'),
        ],
    },
    'government-exam-notes': {
        'title': 'Government Exam Notes | CGE Study Material',
        'description': 'Find government exam notes for RRB NTPC, SSC, UPSC, banking exams, General Awareness, Current Affairs, Reasoning, and Mathematics preparation.',
        'heading': 'Government Exam Notes',
        'intro': 'CGE organizes government exam notes by exam, subject, and topic so aspirants can revise faster and prepare with less confusion.',
        'canonical': '/government-exam-notes',
        'sections': [
            ('Subject-wise notes', 'Study General Awareness, Current Affairs, Reasoning, Mathematics, English, and exam-specific material in a simple structure.'),
            ('Current affairs revision', 'Use monthly current affairs summaries to revise important national, international, sports, economy, and appointment news.'),
            ('Exam-focused learning', 'Focus on notes that match common government exam patterns instead of reading scattered material from many places.'),
        ],
        'faqs': [
            ('Where can I find government exam notes?', 'You can browse CGE for government exam notes organized by exam, subject, and topic.'),
            ('Which notes are important for government exams?', 'Current affairs, static GK, reasoning shortcuts, mathematics formulas, and previous year question patterns are important.'),
        ],
    },
    'rrb-ntpc-notes': {
        'title': 'RRB NTPC Notes | General Awareness and Current Affairs',
        'description': 'Prepare with RRB NTPC notes for General Awareness, Current Affairs, History, Reasoning, and Mathematics on CGE.',
        'heading': 'RRB NTPC Notes',
        'intro': 'RRB NTPC preparation needs consistent revision of General Awareness, Current Affairs, Reasoning, Mathematics, and previous year question patterns.',
        'canonical': '/rrb-ntpc-notes',
        'sections': [
            ('General Awareness notes', 'Revise current affairs, history, geography, polity, economy, science, awards, books, and important railway-related facts.'),
            ('Current affairs for RRB NTPC', 'Monthly current affairs notes help you prepare high-frequency exam topics with quick revision.'),
            ('Practice and revision', 'Combine topic notes with mock tests and previous year questions to improve accuracy before the exam.'),
        ],
        'faqs': [
            ('What should I study for RRB NTPC?', 'Study General Awareness, Mathematics, General Intelligence and Reasoning, current affairs, and previous year questions.'),
            ('Are current affairs important for RRB NTPC?', 'Yes. Current affairs are important for the General Awareness section and should be revised monthly.'),
        ],
    },
}


@app.route('/<slug>')
def seo_landing_page(slug):
    page = SEO_PAGES.get(slug)
    if not page:
        return redirect(url_for('home'))
    return render_template('seo_page.html', page=page, site_url=SITE_URL)


@app.route('/how-to-crack-goverment-exam')
def misspelled_government_exam():
    return redirect(url_for('seo_landing_page', slug='how-to-crack-government-exam'), code=301)

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
    landing_pages = [
        ('how-to-crack-government-exam', '0.9'),
        ('government-exam-notes', '0.9'),
        ('rrb-ntpc-notes', '0.9'),
    ]
    today = date.today().isoformat()
    urls = [
        f"""  <url>
    <loc>{SITE_URL}{url_for(endpoint)}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>"""
        for endpoint, priority in pages
    ]
    urls.extend(
        f"""  <url>
    <loc>{SITE_URL}{url_for('seo_landing_page', slug=slug)}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>"""
        for slug, priority in landing_pages
    )
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
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
