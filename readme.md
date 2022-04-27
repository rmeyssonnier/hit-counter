![Docker Image Size (tag)](https://img.shields.io/docker/image-size/robinmeyssonnier/hit-counter/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/robinmeyssonnier/hit-counter)
![CircleCI](https://img.shields.io/circleci/build/github/rmeyssonnier/hit-counter)
![Codecov](https://img.shields.io/codecov/c/github/rmeyssonnier/hit-counter)

# Hit Counter

A sample POC app create to count http get request. Created initialy to test load balancing.

### How to ?
Run directly in python (tested in python v3.9.12)
```
pip install -r requirements.txt
python app.py
```

Application will bind on port 34001 (on all interfaces).

### Endpoints
To increase counter value : http://127.0.0.1:34001/ -> Will return current value  
To reset counter value : http://127.0.0.1:34001/reset -> Will return success message

### Get from docker hub
```
docker run -p 34001:34001 --name hit-counter -d robinmeyssonnier/hit-counter:latest
````

### Dockerize
It's possible to dockerize application
```
docker build -t hit-counter:latest --no-cache .
docker run -p 34001:34001 --name hit-counter -d hit-counter:latest
````
