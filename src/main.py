from config import DevConfig
from app import make_app

from aiohttp import web


config = DevConfig().config

if __name__ == "__main__":
    app = make_app()
    web.run_app(
        app,
        host=config["APP_HOST"],
        port=config["APP_PORT"]
    )
