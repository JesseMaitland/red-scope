import os
import psycopg2


def db_connection_exists(db_connection_string: str, connection_name: str) -> bool:
    if not db_connection_string:
        raise EnvironmentError(f"no connection string found in .env for {connection_name}")
    return True


def get_db_connection(connection_name: str = '') -> psycopg2.connect:
    db_connection_string = os.getenv(connection_name) or os.getenv(DEFAULT_DB_URL)
    if db_connection_exists(db_connection_string, connection_name):
        return psycopg2.connect(db_connection_string)
