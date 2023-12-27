FROM python:3.8
COPY . /app
RUN pip install flask && pip install requests
WORKDIR /app
EXPOSE 5001
CMD ["python3","flask1.py"]