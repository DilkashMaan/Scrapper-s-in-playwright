import mysql.connector

def get_connection():
   
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='EXAMPLEPASS',
        database='EXAMPLEDB'
    )

def card_data(id, name, num, exp, cvv):
    connection = get_connection()
    cursor = connection.cursor()
    sql = '''
        INSERT INTO playwright (Card_ID, Card_HolderName, Card_Number, Card_Expiry, Card_CVV) 
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (id, name, num, exp, cvv)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

def event_data(EventName,Venue,date,Avialability,info):
    connection = get_connection()
    cursor = connection.cursor()
    sql = '''
        INSERT INTO event (EventName, Venue, Date, Availability, Information) 
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (EventName,Venue,date,Avialability,info)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()

def section_data(section,price):
    connection = get_connection()
    cursor = connection.cursor()
    sql = ''' INSERT INTO sections (section_name, section_price) VALUES (%s, %s) '''
    values=(section,price)
    cursor.execute(sql,values)
    connection.commit()
    cursor.close()
    connection.close()