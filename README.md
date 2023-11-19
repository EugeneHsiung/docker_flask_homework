# docker_flask_homework

# Part One: Dockerizing a Single Flask Application
1. Create a `Part1` [folder](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part1) that contains `templates` folder, `Dockerfile` file, `app.py` file, `requirements.txt`.
2. Inside the `templates` [folder](https://github.com/EugeneHsiung/docker_flask_homework/tree/main/Part1/templates), create a `about.html` and `base.html` using previous codes.
4. Include packages in `requirements.txt`, [code](https://github.com/EugeneHsiung/docker_flask_homework/blob/main/Part1/app.py) in `app.py`
5. Copy the code in `Dockerfile` file

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


