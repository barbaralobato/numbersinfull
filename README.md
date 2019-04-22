# numbersinfull
Web service to get numbers in full according to informed number.

## Prerequisites

Docker

## How to execute it

### Run docker image from Docker Hub

In a terminal, execute follow command:

```
docker run -p 5000:5000 barbaralobato/numbersinfull_pj_docker:latest
```

### Using local docker image
After cloning the project, in a terminal go to root folder (numbersinfull) and execute follow commands:

Build docker image
```
docker build -t numbersinfull_pj_docker:latest .
```
Run docker image
```
docker run -p 5000:5000 numbersinfull_pj_docker:latest
```
## How to test it

Access follow url, replacing <number> by the number you want to get.

http://127.0.0.1:5000/<number\>

Example:
```
curl http://127.0.0.1:5000/-99999
```
