FROM python:3.12.3-slim-bullseye
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .
CMD bash -c "python app.py"