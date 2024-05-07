from pgsql.conn import curpg

import traceback


class Select(object):

    def user_info(self, sql):
        try:
            curpg.execute(sql)
            rows = curpg.fetchall()
            for row in rows:
                print("--> ", row)
            print("select [user_info] table data ok.")
            return
        except:
            print(traceback.format_exc())
            return
