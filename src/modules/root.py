from flask import render_template

def init(app):
    @app.route('/')
    def module_root():
        return render_template('index.html')
