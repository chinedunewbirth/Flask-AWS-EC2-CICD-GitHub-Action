from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visits (count INTEGER)")
    cursor.execute("INSERT INTO visits SELECT 1 WHERE NOT EXISTS (SELECT * FROM visits)")
    cursor.execute("UPDATE visits SET count = count + 1")
    conn.commit()
    count = cursor.execute("SELECT count FROM visits").fetchone()[0]
    return render_template('index.html', count=count)


if __name__ == '__main__':
    app.run(debug=True)

    