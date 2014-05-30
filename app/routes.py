from app    import app
from flask  import render_template, request, redirect
from forms  import LoginForm

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/post/<int:id>/')
def post(id):
    return render_template('post.html', title = 'Titlish', heading = 'The Head of the post')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', title = 'Log in', form = form, providers = app.config['OPENID_PROVIDERS'])
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title = 'Log in', form = form)



