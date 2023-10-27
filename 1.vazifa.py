import requests

def link_tekshiruvchi(link):
    try:
        response = requests.head(link, timeout=5)
        response.raise_for_status()
        print("Link to'g'ri ishlaydi.")
    except requests.exceptions.RequestException as e:
        print("Xatolik yuz berdi:", e)
        raise SystemExit

link_tekshiruvchi("http://www.example.com")
