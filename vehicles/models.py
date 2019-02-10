from django.db import models
import sqlite3
from sqlite3 import Error
import os.path
import time
from datetime import date


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, db_file)
        conn = sqlite3.connect(db_path)
        #conn = sqlite3.connect(db_file)
        #print(db_path)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Vehicle")

    rows = cur.fetchall()

    for row in rows:
        print(row)


select_all_tasks(create_connection('vehicles.db'))


class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    price = models.CharField(int, blank=False)#blank=False
    date = models.IntegerField(date, null=True)
    '''today = date.today()
    the_date = datetime.date(2007, 12, 5)
    today == date.fromtimestamp(time.time())
    my_date = date(today.year, 6, 24)
    '''
    owner = models.CharField(max_length=50)
    room_type = models.PositiveSmallIntegerField()
    brand_id = models.CharField(int, blank=True)
    category_id = models.CharField(int, blank=True)
