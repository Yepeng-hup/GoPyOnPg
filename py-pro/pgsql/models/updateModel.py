from pgsql.conn import curpg,connpg

import traceback


class Update(object):

    def user_info(self, sql):
        try:
            curpg.execute(sql)
            connpg.commit()
            print("update [user_info] table data ok.")
            return
        except:
            print(traceback.format_exc())
            return