import requests
import json
import pandas as pd

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

    # create a list of cards from all the results scraped by ankiconnect
    cards = []
    card_info = anki_request("cardsInfo", cards=card_ids)
    for card in card_info["result"]:
        card_data = []
        try:
    #         print("Card Front:", card["fields"]["Front"]["value"])
    #         print("Card Back:", card["fields"]["Back"]["value"])
            card_data.append(card["fields"]["Front"]["value"])
            card_data.append(card["fields"]["Back"]["value"])
        
        #sometimes, a result will be invalid, this catches those exceptions
        except:
            print("No front of card")
        
        if len(card_data) == 2: cards.append(card_data)
    
    print(cards)
    #create a dataframe of our cards
    df = pd.DataFrame(cards, columns = ['questions', 'answers'])



if __name__ == "__main__":
    main()