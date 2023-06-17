from setuptools import setup

setup(
    name="salary-calc-fastapi",
    version="0.1.1",
    author="Ryan Gilchrist",
    author_email="ryangilchrist92@outlook.com",
    classifiers=["Programming Language :: Python :: 3", "Topic :: Personal Finance"],
    description="FastAPI server for UK salary calculations",
    install_requires=[
        "fastapi==0.89.1",
        "uvicorn==0.20.0",
        "pydantic==1.10.4",
        "fastapi-restful==0.4.3",
        "httpx==0.23.3",
    ],
    packages=[
        "salary_calc_fastapi",
        "salary_calc_fastapi.endpoints",
        "salary_calc_fastapi.models",
        "salary_calc_fastapi.helpers",
        "salary_calc_fastapi.data",
        "salary_calc_fastapi.tests.utils",
    ],
    python_requires=">=3.10",
)
