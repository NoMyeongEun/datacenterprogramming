FROM python:3.8
COPY . /app
RUN pip install flask && pip install requests
WORKDIR /app
EXPOSE 5002
CMD ["python3","flask2.py"]