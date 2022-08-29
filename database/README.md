To start a `mysql` instance with a default database `test_db` without using `docker-compose`, run the following command.

```bash
docker run --name mysql -d -p 3306:3306 -v $(pwd)/init.sql:/data/application/init.sql -e "MYSQL_ROOT_PASSWORD=P@ssw0rd" -e "MYSQL_DATABASE=config_data" mysql:5.7.32 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --init-file /data/application/init.sql
```

```bash
docker run --link mysql --rm -v $(pwd)/flywayfiles/sql:/flyway/sql -v "/var/run/docker.sock":"/var/run/docker.sock" -v $(pwd)/flywayfiles/conf:/flyway/conf flyway/flyway:7.15 migrate -url="jdbc:mysql://mysql:3306?allowPublicKeyRetrieval=True" -user=root -password=P@ssw0rd -locations=filesystem:/flyway/sql/ -connectRetries=2
```