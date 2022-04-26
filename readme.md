
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

### Dockerize
It's possible to dockerize application
```
docker build -t hit-counter:latest --no-cache .
docker run -p 34001:34001 --name hit-counter -d hit-counter:latest
````
