FROM python:3.8.2


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV IS_DOCKERIZED true
COPY src ./

CMD ["streamlit", "run", "main.py"]
