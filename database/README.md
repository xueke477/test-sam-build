To start a `mysql` instance with a default database `test_db` without using `docker-compose`, run the following command.

```bash
docker run -d -p 3306:3306 -v $(pwd)/init.sql:/data/application/init.sql -e "MYSQL_ROOT_PASSWORD=P@ssw0rd" -e "MYSQL_DATABASE=test_db" mysql:5.7.32 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --init-file /data/application/init.sql
```