#!/usr/bin/python3
"""importing MySQLdb to let python connect to a db"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    mycursor = db.cursor()

    mysql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"

    mycursor.execute(mysql)

    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    db.close()
