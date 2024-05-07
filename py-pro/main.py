from pgsql.dbinit import create_test_tables
from pgsql.models.insertModel import Insert
from pgsql.models.selectModel import Select
from pgsql.models.delModel import Delete
from pgsql.models.updateModel import Update


if __name__ == "__main__":
    i = Insert()
    insert_sql = """
        INSERT INTO user_info (name, age, cla, email, home) VALUES ('hong', 15, 902, 'qq@qq.com', '上海');
    """
    s = Select()
    select_sql = """
        SELECT * FROM user_info;
    """
    d = Delete()
    delete_sql = """
        DELETE FROM user_info WHERE name='tom';
    """
    u = Update()
    update_sql = """
        UPDATE user_info SET name = 'xiaoss' WHERE name = 'xiao';
    """
    create_test_tables()
    print("start insert data.") or i.user_info(insert_sql)
    print("start select data.") or s.user_info(select_sql)
    print("start delete data.") or d.user_info(delete_sql)
    print("start update data.") or u.user_info(update_sql)
