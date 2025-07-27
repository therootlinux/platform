def init(app):
    @app.route('/module1')
    def module1_route():
        return "Hello from module1!"
