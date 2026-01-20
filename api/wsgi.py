from decouple import config

from src.app import create_app

config_name = config('FLASK_CONFIG', 'development')
app = create_app(config_name)

@app.route("/")
def test():
    return "<b>Hello new deploy with ECS</b>"
