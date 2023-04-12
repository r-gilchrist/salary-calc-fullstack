# Salary Calculator

![image](https://user-images.githubusercontent.com/56300878/225398463-8f8417d1-5f06-47fe-9606-3f4ef76a0b64.png)

This repository houses a salary calculator using the following technologies:

- `Python` (`FastAPI`)
- `TypeScript`
- `html`, `css`
- `Docker` (a `docker-compose` stack with `nginx` and `Python` containers)

It is based on combining a few other projects on my profile. I got reasonably far building a [backend server in Flask](https://github.com/r-gilchrist/salary_calculator), and wanted to develop my skills in an alternative framework (in this case, `FastAPI`). Similarly, I had a [frontend built in TypeScript](https://github.com/r-gilchrist/salary-calculator-typescript), but wanted to link it to a more sophisticated backend in `Python`, rather than monkey-patching additional bits into the frontend source code.

## Usage

- [Download docker desktop](https://www.docker.com/products/docker-desktop/) and enable WSL2 integration
- In another terminal (you are free to close the one from above), navigate to the root directory of this project.
- `docker-compose up -d` will build the stack
- Navigate to http://localhost/html/home.html in your browser of choice
