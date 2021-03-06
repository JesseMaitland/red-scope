from redscope.schema_introspection.db_objects.ddl import DDL


class User(DDL):

    @property
    def file_name(self) -> str:
        return f"{self.name}.sql"

    @property
    def create(self) -> str:
        return f"CREATE USER {self.name} WITH PASSWORD 'xxxxxxxxxx';"

    @property
    def create_if_not_exist(self) -> str:
        return f"CREATE USER {self.name} WITH PASSWORD 'xxxxxxxxxx';"

    @property
    def drop(self) -> str:
        return f"DROP USER {self.name};"

    @property
    def drop_if_exist(self) -> str:
        return f"DROP USER {self.name};"
