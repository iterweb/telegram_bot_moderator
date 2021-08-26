import sqlite3


class DataWriter:
    def __init__(self):
        self.conn = sqlite3.connect('data.sqlite3')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id TEXT NOT NULL,
            user_name TEXT,
            full_name TEXT,
            date_time TEXT,
            message TEXT,
            active_time INTEGER
            );
            """
        )
        self.conn.commit()

    def get_user_msg(self, user_id):
        self.cur.execute(f"SELECT message, active_time FROM users WHERE tg_id = '{str(user_id)}';")
        user_info = self.cur.fetchall()
        return user_info

    def get_user_info(self, name):
        self.cur.execute(f"SELECT tg_id, full_name, date_time FROM users WHERE full_name = '{name}';")
        db_user = self.cur.fetchall()
        print(db_user)
        return db_user

    def get_user_name(self, user_id):
        self.cur.execute(f"SELECT full_name FROM users WHERE tg_id = '{user_id}';")
        name_user = self.cur.fetchall()
        return name_user[0][0]

    def get_all_users_id(self):
        user_data = []
        self.cur.execute("SELECT tg_id FROM users;")
        db_users = self.cur.fetchall()

        for i in db_users:
            user_data.append(''.join(i))

        return user_data

    def save_user_data(self, tg_id, user_name, full_name, date_time, msg, timestamp):
        self.cur.execute(f"""INSERT INTO users(tg_id, user_name, full_name, date_time, message, active_time)
                           VALUES('{tg_id}', '{user_name}', '{full_name}', '{date_time}', '{msg}', '{timestamp}');""")
        self.conn.commit()

    def update_user_data(self, user_tg_id, username, fullname, datetime, msg, timestamp):
        self.cur.execute(f"""UPDATE users 
                                SET date_time = '{datetime}',
                                    user_name = '{username}',
                                    full_name = '{fullname}',
                                    message = '{msg}',
                                    active_time = '{timestamp}'
                                WHERE tg_id = '{user_tg_id}'
                        """)
        self.conn.commit()

