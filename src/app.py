from interpreter import InterpreterView

from aiohttp import web


def make_app():
    app = web.Application()
    app.add_routes(
        [
            web.view("/api/v1/interpreter", InterpreterView),
        ]
    )
    return app