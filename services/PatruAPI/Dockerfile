FROM python:3.7

WORKDIR /features
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --ignore-installed
ADD . /features

#CMD python3 src/app.py
CMD ["uwsgi", "--ini", "wsgi.ini"]
