from flask import Flask,jsonify
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route("/")
def dbConnection():
    db = mysql.connector.connect(
        user=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DATABASE")
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'; ")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return jsonify({"msg":result[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
                            




