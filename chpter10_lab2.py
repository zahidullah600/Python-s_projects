import sqlite3

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

cursor.execute("DELETE FROM accounts")

accounts = [
    (1, "Ahmad", 1000),
    (2, "Mahmood", 500)
]

cursor.executemany(
    "INSERT INTO accounts VALUES (?, ?, ?)",
    accounts
)

conn.commit()

def display_balances():
    cursor.execute("SELECT * FROM accounts")
    records = cursor.fetchall()

    for record in records:
        print(record)

def transfer(from_id, to_id, amount):
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if from_id == to_id:
            raise ValueError("Accounts must be different")

        cursor.execute("BEGIN TRANSACTION")

        cursor.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (from_id,)
        )

        source = cursor.fetchone()

        cursor.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (to_id,)
        )

        destination = cursor.fetchone()

        if source is None or destination is None:
            raise ValueError("Account not found")

        if source[0] < amount:
            raise ValueError("Insufficient balance")

        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )

        if cursor.rowcount != 1:
            raise ValueError("Debit operation failed")

        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )

        if cursor.rowcount != 1:
            raise ValueError("Credit operation failed")

        conn.commit()
        print("Transfer successful!")

    except Exception as error:
        conn.rollback()
        print("Transfer failed:", error)

print("Balances Before Transfer:")
display_balances()

transfer(1, 2, 300)

print("\nBalances After Transfer:")
display_balances()

conn.close()