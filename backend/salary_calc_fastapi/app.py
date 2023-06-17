from fastapi import FastAPI
from fastapi_restful import Api
from fastapi.middleware.cors import CORSMiddleware
from salary_calc_fastapi.endpoints.salary_calculation import SalaryCalculation


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api = Api(app)
    api.add_resource(SalaryCalculation(), "/salary")
    return app


app = create_app()
