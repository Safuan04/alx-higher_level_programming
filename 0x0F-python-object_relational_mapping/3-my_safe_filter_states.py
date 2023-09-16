#!/usr/bin/python3
"""importing MySQLdb that connects python to a db"""


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

    mysql = ("""SELECT * FROM states
                WHERE name LIKE BINARY %s""")
    user_input = (argv[4],)

    mycursor.execute(mysql, user_input)

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
