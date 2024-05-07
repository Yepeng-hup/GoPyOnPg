import psycopg2


# pgsql conn dict
conn_params = {
    "dbname": "testpg",
    "user": "testpg",
    "password": "xxxx",
    "host": "127.0.0.1",
    "port": 30040,
}
connpg = psycopg2.connect(**conn_params)
curpg = connpg.cursor()

