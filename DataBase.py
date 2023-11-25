import pymysql
from contextlib import contextmanager


class DataBase:
    def __init__(self, host, port, user, password, database, pool_size=4):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.pool_size = pool_size
        self.connection_pool = []

    @contextmanager
    def get_connection(self):
        if not self.connection_pool or len(self.connection_pool) < self.pool_size:
            connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.connection_pool.append(connection)
        else:
            connection = self.connection_pool.pop()
        try:
            yield connection
        finally:
            self.connection_pool.append(connection)

    def execute_query(self, query, params=None):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                try:
                    if params is None:
                        cursor.execute(query)
                    elif isinstance(params, tuple):
                        cursor.execute(query, params)
                    elif isinstance(params, list):
                        cursor.executemany(query, params)
                    else:
                        raise ValueError(
                            "Invalid params type. Should be tuple or list."
                        )
                    result = cursor.fetchall()
                    connection.commit()
                    return result
                except Exception as e:
                    print(f"Error executing query: {e}")
                    connection.rollback()
                    raise
