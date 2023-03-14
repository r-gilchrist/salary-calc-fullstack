# Salary Calculator

![image](https://user-images.githubusercontent.com/56300878/225023796-c27d23ce-da25-489e-aa28-71ec6391ce29.png)

This repository houses a salary calculator using the following technologies:

- `Python` (`FastAPI`)
- `TypeScript`
- `html`, `css`
- `Docker` (a `docker-compose` stack with `nginx` and `Python` containers)

It is based on combining a few other projects on my profile. I got reasonably far building a [backend server in Flask](https://github.com/r-gilchrist/salary_calculator), and wanted to develop my skills in an alternative framework (in this case, `FastAPI`). Similarly, I had a [frontend built in TypeScript](https://github.com/r-gilchrist/salary-calculator-typescript), but wanted to link it to a more sophisticated backend in `Python`, rather than monkey-patching additional bits into the frontend source code.

## Usage

- [Download docker desktop](https://www.docker.com/products/docker-desktop/) and enable WSL2 integration 
- In a terminal, navigate to `root/frontend` and run `tpm start`. This will build the required `JavaScript` files.
- In another terminal (you are free to close the one from above), navigate to the root directory of this project.
- `docker-compose up -d` will build the stack
- Navigate to http://localhost/home.html in your browser of choice
