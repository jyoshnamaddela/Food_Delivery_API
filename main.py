from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Food Delivery API"}


@app.get("/menu")
def get_menu():
    connection = sqlite3.connect("food_delivery.db")
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.execute(
            "SELECT item_id, item_name, price FROM menu_items"
        )
        items = [dict(row) for row in cursor.fetchall()]
        return {"menu": items}
    finally:
        connection.close()


@app.post("/menu")
def add_menu_item(item_name: str, price: float):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO menu_items (restaurant_id, item_name, price) VALUES (?, ?, ?)",
            (1, item_name, price)
        )
        connection.commit()

        return {
            "message": "Food item added successfully",
            "item_name": item_name,
            "price": price
        }
    finally:
        connection.close()