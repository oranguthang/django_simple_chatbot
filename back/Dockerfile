FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /app/back
COPY requirements.txt /app/back
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
