FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt
RUN pip install fastapi uvicorn


COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]