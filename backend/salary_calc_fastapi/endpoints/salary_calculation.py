from fastapi_restful import Resource


class SalaryCalculation(Resource):

    def get(self):
        return {"hello": "world"}
