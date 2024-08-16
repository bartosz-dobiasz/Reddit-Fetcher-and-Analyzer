import sqlite3
from config import DATABASE_FILE
from datetime import datetime


# Create a database connection
def create_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    return conn

# Create the top_posts table if it doesn't exist


def create_table_posts(conn):
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        title TEXT,
        selftext TEXT,
        url TEXT,
        permalink TEXT,
        id TEXT PRIMARY KEY,
        score INTEGER,
        num_comments INTEGER,
        created_utc REAL,
        author TEXT,
        subreddit TEXT,
        is_video BOOLEAN,
        link_flair_text TEXT,
        over_18 BOOLEAN,
        attribute TEXT
        )
    ''')

# convert Unix timestamp to datetime


def convert_utc_to_local(utc_timestamp):
    dt = datetime.utcfromtimestamp(utc_timestamp)
    return dt.strftime('%Y-%m-%d %H:%M:%S')
