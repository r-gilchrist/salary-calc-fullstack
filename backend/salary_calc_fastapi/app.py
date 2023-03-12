from fastapi import FastAPI
from fastapi_restful import Api
from fastapi.middleware.cors import CORSMiddleware
from salary_calc_fastapi.endpoints.hello_world import HelloWorld


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True
    )

    api = Api(app)
    api.add_resource(HelloWorld(), "/helloworld")
    return app


app = create_app()
