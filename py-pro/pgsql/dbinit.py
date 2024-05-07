from pgsql.conn import connpg, curpg

import traceback


def show_pg_all_table():
    curpg.execute(
        "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")

    # show all table
    tables = curpg.fetchall()
    table_names_list = [table[0] for table in tables]
    return table_names_list


def create_test_tables():
    create_table_user_info_sql = """
    CREATE TABLE IF NOT EXISTS user_info (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        cla INT,
        email VARCHAR(255),
        home VARCHAR(255) 
    );
    """
    t = show_pg_all_table()
    if len(t) == 0:
        try:
            curpg.execute(create_table_user_info_sql)
            connpg.commit()
            print("tables [user_info] create ok.")
            return
        except:
            print("error, tables [user_info] create fail.")
            print(traceback.format_exc())
