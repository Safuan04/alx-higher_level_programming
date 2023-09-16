#!/usr/bin/python3
"""Importing MySQLdb that let python connect to a database"""


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

    mysql = """SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s"""

    user_input = (argv[4],)

    mycursor.execute(mysql, user_input)
    result = mycursor.fetchall()

    city_names = [row[0] for row in result]
    conct_city_names = ", ".join(city_names)
    print(conct_city_names)

    mycursor.close()
    mydb.close()
