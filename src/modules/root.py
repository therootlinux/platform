def init(app):
    @app.route('/module1')
    def module_root():
        return "Landing Here!"
