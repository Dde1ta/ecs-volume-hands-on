FROM python:3.12-alpine

WORKDIR /app

RUN mkdir "/dev/data"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app"]
