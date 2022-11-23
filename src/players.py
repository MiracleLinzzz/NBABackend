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
            password="Aa123456",
            # host='nba-players.cjcgoinyvwrv.us-east-1.rds.amazonaws.com',
            host='localhost',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM NBA_PLAYERS.PLAYER_TEAM_SEASON_STATS where PLAYER_ID=%s order by SEASON DESC;"
        conn = NbaPlayerResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=key)
        result = {}
        queries = cur.fetchall()
        for query in queries:
            if result.get(query["SEASON_TYPE"]) == None:
                result[query["SEASON_TYPE"]] = []
            result[query["SEASON_TYPE"]].append(query)
        result["CURRENT_TEAM"] = queries[0]["TEAM_ID"]

        # print(result)

        return result

    @staticmethod
    def get_players():
        sql = "SELECT * FROM NBA_PLAYERS.PLAYER_BASICS order by FIRST_NAME, LAST_NAME;"
        conn = NbaPlayerResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        return result
