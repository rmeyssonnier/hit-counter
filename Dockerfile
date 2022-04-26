FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

EXPOSE 34001

ENV FLASK_APP=app.py

CMD ["python", "app.py"]
