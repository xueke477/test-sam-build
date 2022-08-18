FROM mysql:5.7.32
RUN /entrypoint.sh
COPY ./database/init.sql /data/application/init.sql
CMD [ "mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_unicode_ci", "--init-file", "/data/application/init.sql" ]