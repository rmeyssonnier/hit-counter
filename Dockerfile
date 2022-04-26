FROM python:3.9-alpine as BUILD

WORKDIR /app
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
COPY requirements.txt .
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.9-alpine as RUN

WORKDIR /app
COPY --from=BUILD /app /app
COPY app.py ./

EXPOSE 34001
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "app.py"]
