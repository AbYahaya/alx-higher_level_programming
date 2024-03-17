#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)

    username = args[1]
    password = args[2]
    database = args[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=3306)
        cur = db.cursor()

        # Execute SQL query
        num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY states.id;")
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
