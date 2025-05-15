import requests

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return None

def display_items(data):
    if data is None:
        print("Aucune donnée à afficher.")
        return
    for item in data:
        print(f"Nom: {item['name']}")
        print(f"Description: {item['description']}")
        print("Spécifications:")
        for key, value in item['specifications'].items():
            print(f"  - {key}: {value}")
        print(f"Tags: {', '.join(item['tags'])}")
        print("-" * 40)

if __name__ == "__main__":
    url = "https://<username>.github.io/<repository-name>/custom_data.json"
    json_data = fetch_json_data(url)
    display_items(json_data)
