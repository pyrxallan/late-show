#!/usr/bin/env python3
from app import create_app
from models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    db.session.commit()

    restaurants = [
        Restaurant(name="Luigi's Pizzeria", address="123 Main St, New York, NY"),
        Restaurant(name="Pizza Palace", address="456 Oak Ave, Los Angeles, CA"),
        Restaurant(name="Artisan Slice", address="789 Pine Rd, Chicago, IL"),
    ]
    for r in restaurants:
        db.session.add(r)
    db.session.commit()

    pizzas = [
        Pizza(name="Margherita", ingredients="tomato, mozzarella, basil, olive oil"),
        Pizza(name="Pepperoni", ingredients="tomato, mozzarella, pepperoni"),
        Pizza(name="Veggie Deluxe", ingredients="tomato, mozzarella, bell peppers, onions, mushrooms"),
        Pizza(name="BBQ Chicken", ingredients="BBQ sauce, chicken, cheddar, red onion"),
        Pizza(name="Quattro Formaggi", ingredients="mozzarella, parmesan, gorgonzola, ricotta"),
    ]
    for p in pizzas:
        db.session.add(p)
    db.session.commit()

    links = [
        RestaurantPizza(restaurant_id=1, pizza_id=1, price=12.99),
        RestaurantPizza(restaurant_id=1, pizza_id=2, price=13.99),
        RestaurantPizza(restaurant_id=1, pizza_id=3, price=14.99),
        RestaurantPizza(restaurant_id=2, pizza_id=2, price=14.99),
        RestaurantPizza(restaurant_id=2, pizza_id=4, price=15.99),
        RestaurantPizza(restaurant_id=3, pizza_id=1, price=11.99),
        RestaurantPizza(restaurant_id=3, pizza_id=5, price=16.99),
    ]
    for link in links:
        db.session.add(link)
    db.session.commit()

    print("Database seeded successfully!")
    print(f"Created {len(restaurants)} restaurants")
    print(f"Created {len(pizzas)} pizzas")
    print(f"Created {len(links)} restaurant-pizza links")
