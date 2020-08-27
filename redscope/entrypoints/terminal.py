from typing import Callable
from rsterm import EntryPoint
from redscope.env.file_paths import FilePaths
from redscope.schema_introspection.db_introspection import \
    introspect_tables, introspect_schemas, introspect_users, \
    introspect_constraints, introspect_groups, introspect_user_groups, \
    introspect_views, introspect_db, DbIntrospection, DbCatalog


class IntroDb(EntryPoint):

    entry_point_args = {
        ('db_object', ): {
            'help': 'the name of the object you would like to introspect',
            'choices': DbIntrospection.allowed_db_objects + ['all']
        },

        ('--save', '-s'): {
            'help': 'set this flag to save introspected objects to files. All existing files will be overwritten',
            'action': 'store_true'
        }
    }

    function_map = {
        'tables': introspect_tables,
        'schemas': introspect_schemas,
        'users': introspect_users,
        'constraints': introspect_constraints,
        'groups': introspect_groups,
        'views': introspect_views,
        'usergroups': introspect_user_groups,
        'all': introspect_db
    }

    def run(self) -> None:
        introspection_function = self.lookup_function()
        db_connection = self.rsterm.get_db_connection('redscope')

        db_catalog: DbCatalog = introspection_function(db_connection)

        file_paths = FilePaths()

        if self.cmd_args.save:

            if self.cmd_args.db_object == 'all':
                objects_to_save = [key for key in self.function_map.keys() if key != 'all']
            else:
                objects_to_save = [self.cmd_args.db_object]

            file_paths.save_files(db_catalog, *objects_to_save)
        exit()

    def lookup_function(self) -> Callable:
        return self.function_map[self.cmd_args.db_object]
