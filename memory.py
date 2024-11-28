import sqlite3

class MemoryManager:
    def __init__(self, db_name='memory.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY,
                    user_input TEXT,
                    response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def store_interaction(self, user_input, response):
        with self.conn:
            self.conn.execute('INSERT INTO interactions (user_input, response) VALUES (?, ?)', (user_input, response))

    def get_context(self, user_input):
        with self.conn:
            cursor = self.conn.execute('SELECT user_input, response FROM interactions ORDER BY timestamp DESC LIMIT 5')
            context = cursor.fetchall()
        return context
