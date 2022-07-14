From python:3.10-slim

COPY . ./flask_app

WORKDIR /flask_app

RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install gunicorn

# ENV FLASK_APP=app

# ENV DATABASE_URL=mysql+pymysql://root:root@127.0.0.1:3306/flask_app

RUN chmod 755 run_sh.sh

ENTRYPOINT ["/bin/sh", "./run_sh.sh" ]