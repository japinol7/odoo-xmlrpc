__author__ = 'Joan A. Pinol  (japinol)'

DEFAULT_LIMIT = 50


class XmlRpcClient:
    """Represents a xml-rpc client."""

    def __init__(self, connection):
        self._connection = connection.models
        self._common = connection.common
        self._server = connection.server
        self._uid = connection.uid

    def get_db_list(self):
        """Gets the available databases."""
        raise Exception("Not implemented yet for xmlrpc.")

    def get_server_version(self):
        """Gets the server version."""
        return self._common.version()['server_version']

    def get_server_version_data(self):
        """Gets the server version data."""
        return self._common.version()

    def call_service(self, service_obj_name, method, kwargs=None):
        """Calls a given method on a given service object name with
        the specified kwargs. Service name examples: common, db, object.
        """
        raise Exception("Not implemented yet for xmlrpc.")

    def call_common(self, method, kwargs=None):
        """Calls a given method on the common service
        with the specified kwargs.
        """
        raise Exception("Not implemented yet for xmlrpc.")

    def call_db(self, method, kwargs=None):
        """Calls a given method on the db service
        with the specified kwargs.
        """
        raise Exception("Not implemented yet for xmlrpc.")

    def call(self, model_obj_name, method, ids, args=None, kwargs=None):
        """Calls a given method on given model object instances
        with the specified positional args and kwargs.
        Recommended way to call a normal recordset method.
        """
        ids = ids or []
        args = args or []
        args = [ids] + args

        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            method, args, kwargs or {},
            )

    def call_on_model(self, model_obj_name, method, args=None, kwargs=None):
        """Calls a given method on a given model object name
        with the specified positional args and kwargs.
        Recommended way to call an api.model method.
        """
        if kwargs is None:
            return self._connection.execute_kw(
                self._server.dbname, self._uid, self._server.password,
                model_obj_name,
                method, args or [],
                )

        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            method, args or [], kwargs or {},
            )

    def create(self, model_obj_name, values):
        """Creates a document object with the specified values."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'create', values,
            )

    def read(self, model_obj_name, ids, fields):
        """Gets the values of the document object for the specified ids."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'read', ids, fields,
            )

    def read_group(
            self, model_obj_name, domain, fields, group_by, limit=DEFAULT_LIMIT
        ):
        """Returns a list of dictionaries with the aggregate results
        grouped by the `group_by` field.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'read_group', domain,
            {'fields': fields, 'groupby': group_by, 'limit': limit},
            )

    def search(self, model_obj_name, domain, order=None, limit=DEFAULT_LIMIT):
        """Gets the ids of the document object that match the specified domain."""
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search', domain,
            {'order': order, 'limit': limit},
            )

    def search_count(self, model_obj_name, domain):
        """Returns the number of ids for the document object that match the
        specified domain.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search_count', domain,
            )

    def search_read(
            self, model_obj_name, domain, fields, order=None, limit=DEFAULT_LIMIT
        ):
        """Combines the search and read operations in one call.
        Returns a list of dictionaries with the required fields for each object
        that matches the specified domain.
        """
        return self._connection.execute_kw(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'search_read', domain,
            {'fields': fields, 'order': order, 'limit': limit},
            )

    def write(self, model_obj_name, ids, values):
        """Updates the document objects for the specified ids with the specified
        values.
        """
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'write', ids, values,
            )

    def unlink(self, model_obj_name, ids):
        """Deletes the document objects that match the specified ids."""
        return self._connection.execute(
            self._server.dbname, self._uid, self._server.password,
            model_obj_name,
            'unlink', ids,
            )
