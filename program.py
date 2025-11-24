import pymysql
from datetime import datetime
conn=pymysql.connect(host='localhost', user='root', password='nimrutha12', database='logistics_db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS packages (package_id INTEGER PRIMARY KEY auto_increment,sender VARCHAR(255),recipient VARCHAR(255),status VARCHAR(255),last_update VARCHAR(255))''')
cur.execute('''CREATE TABLE IF NOT EXISTS delivery_person (person_id INTEGER PRIMARY KEY auto_increment,name VARCHAR(255),contact VARCHAR(255))''')
def add_pack(sender, recipient):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO packages (sender, recipient, status, last_update) VALUES (%s, %s, %s, %s)",(sender, recipient, 'Dispatched', now))
    conn.commit()
    print(f"Package added for {recipient} sent by {sender}.")
def update_pack_status(p_id, new_status):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("UPDATE packages SET status=%s, last_update=%s WHERE package_id=%s",(new_status, now, p_id))
    conn.commit()
    print(f"Package {p_id} status updated to {new_status}.")
def get_pack_info(p_id):
    cur.execute("SELECT * FROM packages WHERE package_id=%s", (p_id,))
    pa=cur.fetchone()
    if pa:
        print(f"Package ID: {pa[0]}\nSender: {pa[1]}\nRecipient: {pa[2]}\nStatus: {pa[3]}\nLast Update: {pa[4]}")
    else:
        print("Package not found.")
def add_del_person(n, con):
    cur.execute("INSERT INTO delivery_person (name, contact) VALUES (%s, %s)",(n, con))
    conn.commit()
    print(f"Delivery person {n} added.")
def get_del_person(person_id):
    cur.execute("SELECT * FROM delivery_person WHERE person_id=%s", (person_id,))
    person=cur.fetchone()
    if person:
        print(f"Personnel ID: {person[0]}\nName: {person[1]}\nContact: {person[2]}")
    else:
        print("Delivery person not found.")
# Example usage:
add_pack('Alice', 'Bob')
add_del_person('Charlie', '123-456-7890')
get_pack_info(1)
get_del_person(1)
update_pack_status(1, 'In Transit')
get_pack_info(1)
