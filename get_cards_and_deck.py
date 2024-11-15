import requests
import json

ANKI_CONNECT_URL = 'http://localhost:8765'

def anki_request(action, **params):
    request_payload = json.dumps({
        "action": action,
        "version": 6,
        "params": params
    })
    #print(params)
    response = requests.post(ANKI_CONNECT_URL, data=request_payload)
    return response.json()

def main():
    # print('Enter a deck name:')
    # deck_name = input()

    deck_name = "[A]_Biology::Biology_Paper_1::Biology_-_B3_Infection_and_Response"  # replace with your deck name
    testquery = f"deck:{deck_name}"
    cards = anki_request("findCards", query=testquery)
    card_ids = cards["result"]
    print("Card IDs from sample deck")
    print(card_ids)

    print("------------")

    # get deck id from specific list of cards
    card_deck = anki_request("getDecks", cards=card_ids)
    print("All decks used by above IDs, should only be one deck")
    print(card_deck["result"])


if __name__ == "__main__":
    main()