import pymysql

import os


class NbaPlayerResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("DBUSER")
        # pw = os.environ.get("DBPW")
        # h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user="root",
            password="dbuserdbuser",
            host='nba-players.cjcgoinyvwrv.us-east-1.rds.amazonaws.com',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM NBA_PLAYERS.PLAYER_TEAM_SEASON_STATS where PLAYER_ID=%s;"
        conn = NbaPlayerResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

