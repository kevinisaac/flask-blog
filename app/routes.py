from app    import app
from flask  import render_template

@app.route('/')
def index():
    return render_template('index.html', title   = "I earned this title")

@app.route('/post/<int:title>')
def post(title):
    return render_template('post.html')
