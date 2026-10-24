Food Delivery API

A REST API built using Python and FastAPI to manage food menu items.

Features

- Get a welcome message
- View all food menu items
- Add new food items
- Store menu data using SQLite
- Interactive API testing using Swagger UI

Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- GitHub
- Render

API Endpoints

Method| Endpoint| Description
GET| "/"| Display welcome message
GET| "/menu"| View food menu
POST| "/menu"| Add a food item

Live Demo

Live API: Replace this line with your Render URL.

API Documentation:  https://food-delivery-apij.onrender.com

How to Run Locally

1. Clone this GitHub repository.

2. Install the required packages:
   
   "pip install -r requirements.txt"

3. Start the server:
   
   "uvicorn main:app --reload"

4. Open "http://127.0.0.1:8000/docs" in your browser.

Database

This project uses SQLite to store food menu items. Persistent storage should be configured for reliable online data retention.

Project Status

Deployed on Render and tested using the available API endpoints.
