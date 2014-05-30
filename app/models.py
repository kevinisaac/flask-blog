from app        import db
from datetime   import datetime

class Category(db.Model):

    __tablename__   = 'categories'

    id              = db.Column(db.Integer, primary_key = True)
    name            = db.Column(db.String(100))
    slug            = db.Column(db.String(100))
    post_count      = db.Column(db.Integer, default = 0)

    def __init__(self, name, slug, post_count): 
        self.name           = name
        self.slug           = slug
        self.post_count     = post_count
        self.created        = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Category - %s>' % (self.name)

category = Category('a','a',2)

class Comment(db.Model):

    __tablename__   = 'comments'

    id              = db.Column(db.Integer, primary_key = True)
    post_id         = db.Column(db.Integer)
    username        = db.Column(db.String(50))
    mail            = db.Column(db.String(80))
    content         = db.Column(db.String(2000))
    created         = db.Column(db.DateTime)

    def __init__(self, post_id, username, mail, content): 
        self.post_id        = post_id
        self.username       = username
        self.mail           = mail
        self.content        = content
        self.created        = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Comment - %s>' % (self.content)

class Post(db.Model):

    __tablename__   = 'posts'

    id              = db.Column(db.Integer, primary_key = True)
    category_id     = db.Column(db.Integer)
    user_id         = db.Column(db.Integer) 
    name            = db.Column(db.String(300))
    slug            = db.Column(db.String(300))
    content         = db.Column(db.String(8000))
    created         = db.Column(db.DateTime)
    
    def __init__(self, category_id, user_id, name, slug, content): 
        self.category_id    = category_id
        self.user_id        = user_id
        self.name           = name
        self.slug           = slug
        self.content        = content
        self.created        = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return '<Post - %s>' % (self.name)

class User(db.Model):

    __tablename__   = 'users'

    id              = db.Column(db.Integer, primary_key = True)
    username        = db.Column(db.String(50))
    password        = db.Column(db.String(80))

    def __init__(self, username, password): 
        self.username       = username
        self.password       = password

    def __repr__(self):
        return '<User - %s>' % (self.username)
