FROM python:3.8.2


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY src ./

CMD ["streamlit", "run", "main.py"]
