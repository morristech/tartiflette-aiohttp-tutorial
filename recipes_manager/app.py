import os

from aiohttp import web

from tartiflette_aiohttp import register_graphql_handlers


def run():
    app = web.Application()

    web.run_app(
        register_graphql_handlers(
            app=app,
            engine_sdl=os.path.dirname(os.path.abspath(__file__)) + "/sdl",
            engine_modules=[
                "recipes_manager.query_resolvers",
                "recipes_manager.mutation_resolvers",
                "recipes_manager.subscription_resolvers",
                "recipes_manager.directives.rate_limiting",
                "recipes_manager.directives.auth",
            ],
            subscription_ws_endpoint="/ws",
            executor_http_endpoint='/graphql',
            executor_http_methods=['POST'],
            graphiql_enabled=True
        )
    )
