FROM python:3.6-jessieRUN apt updateWORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /appENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]