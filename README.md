# docker_flask_homework

# Part One: Dockerizing a Single Flask Application
1. Create a `Part1` [folder](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part1) that contains `templates` folder, `Dockerfile` file, `app.py` file, `requirements.txt` in google shell environment
2. Inside the `templates` [folder](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part1/templates), create a `about.html` and `base.html` using previous codes
4. Include packages in `requirements.txt` file
5. Include [code](https://github.com/EugeneHsiung/docker_flask_homework/blob/main/Part1/app.py) in `app.py`
6. Copy the code in `Dockerfile` file:

```
# Use Python 3.7 image for the Docker image
FROM python:3.7-alpine  
# application code placed in the working directory to /app
WORKDIR /app
# Copies content of current directory onto 'app' directory 
COPY . /app
# Installs the requirements in the requirements.txt file
RUN pip install -r requirements.txt 
# use port 5000
EXPOSE 5000
# command to run app.py using python
CMD ["python", "app.py"]
```

6. Type in `docker build -t <image name>` in google shell environment. Replace image name with what you want to build the image.
7. Type in `docker images` to view images
8. Type in `docker run -p 5000:5000 <image name>` to run docker container. You are able to change the ports to whichever one. Make sure to also change the Google shell port environment
9. Type in `docker ps` to view the list of containers

# Part Two: Multi-Container Setup with Docker Compose
1. Create a `Part2` [folder](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part1](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part2)) that contains 2 `Flask` folders each containing a `templates` folder, `Dockerfile` file, `app.py` file, `requirements.txt`
2. Inside each `templates` folder, create a `about.html` and `base.html` using previous codes
3. Include packages in each `requirements.txt` file
4. Include codes in each `app.py` file
5. Copy the [code](https://github.com/EugeneHsiung/docker_flask_homework/blob/main/Part2/Flask1/Dockerfile) in `Dockerfile` file
6. Create a `docker-compose.yml` file
7. Copy the code in `docker-compose.yml` file:

```
version: '3'
services:
  flask_app_1:
    build: ./flask1
    ports:
      - "5001:5000"
    volumes:
      - ./flask1:/app
  flask_app_2:
    build: ./flask2
    ports:
      - "5002:5000"
    volumes:
      - ./flask2:/app
```

8. Type in `docker-compose up --build` to start the services in the `docker-compose.yml` file
9. Type in `docker-compose ps` to get a list of the services
10. Type in `docker-compose up -d` to start Docker services 

