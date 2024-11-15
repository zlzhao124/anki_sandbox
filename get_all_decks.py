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
    # Test to get all decks
    all_decks = anki_request("deckNames")
    print("All Decks:", all_decks["result"])


if __name__ == "__main__":
    main()