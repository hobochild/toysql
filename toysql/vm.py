from typing import List, Any
from toysql.parser import SelectStatement, InsertStatement, CreateStatement, Statement
from toysql.table import Table
from toysql.pager import Pager
from toysql.lexer import StatementLexer
from toysql.parser import Parser
from toysql.lexer import Keyword
import toysql.datatypes as datatypes


# TODO this should be called the executor.
class VM:
    def __init__(self, file_path):
        self.pager = Pager(file_path)
        self.lexer = StatementLexer()
        self.parser = Parser()
        self.tables = {}

    def create_schema_table(self) -> Table:
            # TODO we need to load the schema (cols) from disk.
            # sqlite uses txt.
            columns = {
                "id": datatypes.Integer(),
                "root_page_num": datatypes.Integer(),
                "name": datatypes.String(500),
            }
            return Table(self.pager, columns, 0)

    def create_table(self, table_name, columns) -> Table:
        table = Table(self.pager, columns, 0)
        self.tables[table_name] = table
        return table

    def get_table(self, table_name) -> Table:
        # TODO we should instead read from internal "tables" table.
        return self.tables[table_name]

    def execute(self, input: str) -> List[Any]:
        tokens = self.lexer.lex(input)
        stmts = self.parser.parse(tokens)
        results = []

        for stmt in stmts:
            result = self.execute_statement(stmt)
            results.append(result)

        return results

    def execute_statement(self, statement: Statement):
        if isinstance(statement, SelectStatement):
            table_name = statement._from.value
            return self.get_table(table_name).select()

        if isinstance(statement, InsertStatement):
            table_name = statement.into.value
            return self.get_table(table_name).insert(statement.values)

        if isinstance(statement, CreateStatement):
            breakpoint()
            table_name = statement.table.value

            columns = {}
            for col in statement.columns:
                length = col.length.value if col.length else None
                columns[col.name.value] = datatypes.factory(
                    Keyword(col.datatype.value), length
                )

            return self.create_table(table_name, columns)
