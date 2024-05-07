from pgsql.conn import curpg,connpg

import traceback


class Delete(object):

    def user_info(self, sql):
        try:
            curpg.execute(sql)
            connpg.commit()
            print("delete [user_info] table data ok.")
            return
        except:
            print(traceback.format_exc())
            return