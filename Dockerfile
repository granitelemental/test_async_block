FROM python:3.11

WORKDIR .
COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]