from fastapi import FastAPI
from fastapi_restful import Api
from salary_calc_fastapi.endpoints.hello_world import HelloWorld


def create_app():
    app = FastAPI()
    api = Api(app)
    api.add_resource(HelloWorld(), "/helloworld")
    return app


app = create_app()
