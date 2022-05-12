FROM python:3.8-alpine

COPY ./requirements.txt /techs_dev_test/requirements.txt


WORKDIR /techs_dev_test


RUN pip install -r requirements.txt


COPY . /techs_dev_test

ENTRYPOINT [ "python" ]



CMD ["run.py" ]