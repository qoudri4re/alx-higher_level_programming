#!/usr/bin/python3
""" displays values in the
cities table of htbn_0e_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        database_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = database_connection.cursor()
        cursor.execute(
            "SELECT cities.id, cities.name, " +
            "states.name FROM cities INNER JOIN states " +
            " ON cities.state_id = states.id ORDER BY " +
            " cities.id ASC"
        )
        results = cursor.fecthall()
        for result in results:
            print(result)
        database_connection.close()
