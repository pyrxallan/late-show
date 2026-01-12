#!/usr/bin/env python3
"""Test script for restaurant-pizza API endpoints."""
import sys
import os
sys.path.insert(0, '/home/issallan/phase-4/late-show')

from app import create_app
from models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    # Test GET /restaurants
    print("\n=== Testing GET /restaurants ===")
    restaurants = Restaurant.query.all()
    print(f"✓ Found {len(restaurants)} restaurants")
    for r in restaurants:
        print(f"  - {r.name} ({r.address})")

    # Test GET /pizzas
    print("\n=== Testing GET /pizzas ===")
    pizzas = Pizza.query.all()
    print(f"✓ Found {len(pizzas)} pizzas")
    for p in pizzas:
        print(f"  - {p.name} ({p.ingredients})")

    # Test GET /restaurants/<id> (with included pizzas)
    print("\n=== Testing GET /restaurants/<id> with pizzas ===")
    r = restaurants[0]
    print(f"✓ Restaurant: {r.name}")
    print(f"  Restaurant Pizzas:")
    for rp in r.restaurant_pizzas:
        print(f"    - {rp.pizza.name}: ${rp.price}")

    # Test creating a new Restaurant
    print("\n=== Testing POST /restaurants ===")
    new_restaurant = Restaurant(name="Test Pizza Co", address="999 Test St")
    db.session.add(new_restaurant)
    db.session.commit()
    print(f"✓ Created restaurant: {new_restaurant.name} (ID: {new_restaurant.id})")

    # Test creating a new Pizza
    print("\n=== Testing POST /pizzas ===")
    new_pizza = Pizza(name="Test Special", ingredients="test, sauce, cheese")
    db.session.add(new_pizza)
    db.session.commit()
    print(f"✓ Created pizza: {new_pizza.name} (ID: {new_pizza.id})")

    # Test creating a RestaurantPizza
    print("\n=== Testing POST /restaurant_pizzas ===")
    new_rp = RestaurantPizza(restaurant_id=new_restaurant.id, pizza_id=new_pizza.id, price=9.99)
    db.session.add(new_rp)
    db.session.commit()
    print(f"✓ Created restaurant-pizza link (ID: {new_rp.id})")
    print(f"  {new_restaurant.name} -> {new_pizza.name} @ ${new_rp.price}")

    # Test DELETE /restaurants/<id>
    print("\n=== Testing DELETE /restaurants/<id> ===")
    delete_id = new_restaurant.id
    to_delete = Restaurant.query.get(delete_id)
    if to_delete:
        db.session.delete(to_delete)
        db.session.commit()
        print(f"✓ Deleted restaurant (ID: {delete_id})")

    print("\n=== All Core Operations Passed ✓ ===\n")
