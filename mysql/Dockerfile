FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=root

COPY ./create_db.sql /tmp

CMD [ "mysqld" , "--init-file=/tmp/create_db.sql" ]

EXPOSE 3306