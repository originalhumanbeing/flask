FROM python

RUN mkdir app
ADD services app/services
ADD tasks app/tasks
ADD app.py app
ADD requirements.txt app
WORKDIR app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
