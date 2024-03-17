#!/usr/bin/python3
"""
Created by Ab Yahaya
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print("Usage: {} username password database_name state_name"
              .format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    database = args[3]
    state_name = args[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost', user=username
                             passwd=password, db=database, port=3306)
        cur = db.cursor()

        # Execute SQL query
        num_rows = cur.execute("SELECT * FROM states WHERE states.name\
                               LIKE BINARY '{}' ORDER BY states.id;"
                               .format(state_name))
        rows = cur.fetchall()

        # Print query results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
