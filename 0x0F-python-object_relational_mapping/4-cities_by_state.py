#!/usr/bin/python3
"""Importing MySQLdb to let python connect with a db"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    mycursor = mydb.cursor()

    mysql = """SELECT cities.id, cities.name, states.name AS s_n
                FROM cities
                JOIN states ON cities.state_id = states.id"""

    mycursor.execute(mysql)

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
