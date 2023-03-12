# Salary Calculator

This repository houses a salary calculator using the following technologies:

- Python (FastAPI)
- TypeScript
- html, css
- Docker (a `docker-compose` stack with `nginx` and `Python` containers)

It is based off of some previous work over a few other repositories on my profile. I got quite far building a backend server in Flask, and also started a frontend in TypeScript/Node, and thought bringing them all together in one place would be a good idea.

## Installation

- Download docker desktop and enable WSL2 integration https://www.docker.com/products/docker-desktop/
- In a terminal, navigate to the root directory of this project.
- `docker-compose up -d` will build the stack
- Navigate to `localhost:80/hello_world.html` in your browser of choice (webpage to be updated shortly!)
- The website doesn't currently do anything apart from if you look at the logs, where a simple calculation utilising the backend has been performed
