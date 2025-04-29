import mysql.connector

def get_connection():
        return mysql.connector.connect(
        host="mysql-12ad5647-loukrichi4-6ea2.l.aivencloud.com",
        user="avnadmin",         
        password="AVNS_Z_57T7rhtzNvEpcjRSD",     
        database="registration_system",
        port=22332
    )



