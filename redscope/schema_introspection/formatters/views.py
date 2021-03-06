import sqlparse
from typing import Tuple, List
from redscope.schema_introspection.db_objects.view import View
from redscope.schema_introspection.formatters.base_formatter import DDLFormatter


class ViewFormatter(DDLFormatter):

    def __init__(self, raw_ddl: Tuple[str] = None):
        self.raw_ddl = raw_ddl or ()

    def format(self, raw_ddl: Tuple[str]) -> List[View]:
        self.raw_ddl = raw_ddl
        return [View(schema=ddl[0], name=ddl[1], ddl=sqlparse.format(ddl[2], reindent=True)) for ddl in self.raw_ddl]
