
## By Xavier Floyd
### Quick Setup
First, create a database:
```
postgres=#
postgres=# CREATE USER postgres WITH PASSWORD 'jan2001';
CREATE ROLE
postgres=# CREATE DATABASE hw3;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE hw3 to postgres;
GRANT
postgres=# \q
```

Link your database in pgadmin:
```
Name : hw3

Host address: '127.0.0.1' or 'Localhost'
Port: 5432
username: postgres
password: jan2001
```