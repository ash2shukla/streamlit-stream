FROM python:3.8.2-slim-buster


COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt


COPY main.py ./main.py

CMD ["streamlit", "run", "main.py"]
