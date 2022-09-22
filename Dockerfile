FROM python:3.6

ADD . /code

WORKDIR /code

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade -q pip 
RUN pip3 install -q --no-python-version-warning --disable-pip-version-check -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["python3","./app.py"]

EXPOSE 8080

