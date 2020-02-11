from pyhive import hive

host_name = "localhost"  # forward port of server to localhost
port = 10000
user = "hive"
password = "password"
database = "forex"


def hiveconnection(host_name, port, user, password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select * from school')
    result = cur.fetchall()

    return result


# Call above function
output = hiveconnection(host_name, port, user, password, database)
print(output)
