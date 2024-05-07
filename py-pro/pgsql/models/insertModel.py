from pgsql.conn import curpg, connpg

import traceback


class Insert(object):

    def user_info(self, sql):
        try:
            curpg.execute(sql)
            connpg.commit()
            print("insert [user_info] table data ok.")
            return
        except:
            print(traceback.format_exc())
            return

    def xxx(self):
        pass
