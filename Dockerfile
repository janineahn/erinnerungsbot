FROM python:3.6

COPY . ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
CMD ["token"]
