#!/usr/bin/python3
"""importing MySQLdb to connect python to a database"""


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

    mycursor.execute("SELECT * FROM states")

    result = mycursor.fetchall()

    for row in result:
        print(row)

    mycursor.close()
    db.close()
