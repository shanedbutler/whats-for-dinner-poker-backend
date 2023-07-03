from flask import jsonify
from app import app, db
from models import Deck, Suit, Card

@app.route('/api/decks', methods=['GET'])
def get_decks():
    decks = Deck.query.all()
    results = []
    
    for deck in decks:
        results.append({
            "id": deck.id,
            "name": deck.name,
            "description": deck.description
        })

    return jsonify(results)

@app.route('/api/cards?deck=<int:id>', methods=['GET'])
def get_cards_by_deck(id):
    cards = Card.query.filter_by(deck_id=id).all()
    results = []

    for card in cards:
        suit = Suit.query.get(card.suit_id)
        results.append({
            "id": card.id,
            "name": card.name,
            "suit": {
                "id": suit.id,
                "name": suit.name
            },
            "description": card.description,
            "isVegetarian": card.isVegetarian
        })    

    return jsonify(results)
