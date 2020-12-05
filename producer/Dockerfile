FROM python:3.8.2


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY main.py ./main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
