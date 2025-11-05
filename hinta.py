import requests


def hae_sahkon_hinnat():
    url = "https://www.sahkohinta-api.fi/api/v1/halpa?tunnit=24&tulos=sarja"
    response = requests.get(url)
    data = response.json()

    # Poimitaan tiedot
    ajat = [item["aikaleima_suomi"][-5:] for item in data]  # esim. '00:00'
    hinnat = [item["hinta"] for item in data]

    # Tulostetaan taulukkomuodossa
    print("Tunti | Hinta (snt/kWh)")
    print("-----------------------")
    for aika, hinta in zip(ajat, hinnat):
        print(f"{aika:>5} | {hinta:>5.3f}")

    # Lasketaan myös keskiarvo ja halvin/kallein tunti
    min_tunti = min(data, key=lambda x: x["hinta"])
    max_tunti = max(data, key=lambda x: x["hinta"])
    ka = sum(hinnat) / len(hinnat)

    print(" Päivän yhteenveto:")
    
    print(f"  Keskimääräinen hinta: {ka:.2f} snt/kWh")
    print(f"  Halvin tunti: {min_tunti['aikaleima_suomi']} ({min_tunti['hinta']:.2f} snt/kWh)")
    print(f"  Kallein tunti: {max_tunti['aikaleima_suomi']} ({max_tunti['hinta']:.2f} snt/kWh)")


    return hinnat

if __name__ == "__main__":
    hae_sahkon_hinnat()
