import conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def bootstrap(db_file):

    sql_create_nodes_table = """ CREATE TABLE IF NOT EXISTS nodes (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        value text NOT NULL,
                                        parent_id integer,
                                        child_id_csv_str text,
                                        valueset_csv_str text
                                    ); """

    # create a database connection
    conn = conn.db_connect(db_file)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_nodes_table)
    else:
        print("Error! cannot create the database connection.")