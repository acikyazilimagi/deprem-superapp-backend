<div align="center">
    <h1>Deprem Superapp Backend</h1>
    <h3>Basit arayüzlü Deprem Superapp projesinin backendi.</h3>
</div>

<br>

# İçerikler
- [1. Kurulum](#kurulum)
- [2. Kullanışı](#kullanışı)
- [3. Lisans](#lisans)

#  Kurulum
```zsh
$ pip install -r requirements.txt
$ pre-commit install
```

#  Kullanışı
### /get_map_data

```zsh
$ curl --location --request POST 'https://deprem-superapp-backend.herokuapp.com/get_map_data' \
--header 'Content-Type: application/json' \
--data-raw '{
    "notlar": "yemek"
}'

>> {
    "status_code": 200,
    "detail": [
        {
            "_id": "63e586dcf9a73164daa3e8ee",
            "il": "KAHRAMANMARAŞ",
            "ilce": "GÖKSUN",
            "adres": "Hacıkodal Köyü",
            "isim": "Mehmet Akkul",
            "gereksinimler": [
                "Yemek"
            ],
            "telefon": "5316370736",
            "lat": 37.915747,
            "lon": 36.304464,
            "notlar": "köyün acil yemek ihtiyacı var",
            "zaman": "2023-02-10T02:50:52.050000"
        },
        ...
        {
            "_id": "63e586d8f9a73164daa3e8a4",
            "il": "KAHRAMANMARAŞ",
            "ilce": "KARAELBİSTAN",
            "adres": "nizam sokak",
            "isim": "-",
            "gereksinimler": [
                "Yemek",
                "Giyim"
            ],
            "telefon": "0505 046 4846",
            "lat": 38.2014344,
            "lon": 37.1393996,
            "notlar": "yemek su kıyafet hiç bir şey gitmemiş öğrenciler vesaire varmış adreste depremden beri aç ve susuzlar bi yakınım ulaştırdı",
            "zaman": "2023-02-10T02:50:48.215000"
        }
    ],
    "headers": null
}
```

### /set_map_data
```zsh
$ curl --location --request POST 'https://deprem-superapp-backend.herokuapp.com/set_map_data' \
--header 'Content-Type: application/json' \
--data-raw '{
  "il": "Ankara",
  "ilce": "string",
  "adres": "string",
  "isim": "string",
  "gereksinimler": [
    "string",
    "string",
    "string",
    "string",
    "string"
  ],
  "telefon": "string",
  "lat": 0,
  "lon": 0,
  "notlar": "string",
  "zaman": "2023-02-09T08:45:51.062Z"
}'

>> "63e586d4f9a73164daa3e85e"  // ObjectId of the inserted data
```

### /get_service_point
```zsh
$ curl --location --request POST 'https://deprem-superapp-backend.herokuapp.com/get_service_point' \
--header 'Content-Type: application/json' \
--data-raw '{
  "il": "",
  "ilce": "",
  "servis": [],
  "notlar": "otobüs"
}'

>> {
    "status_code": 200,
    "detail": [
        {
            "_id": "63e575aa3e74c8a97dfc4935",
            "il": "HATAY",
            "ilce": "ANTAKYA",
            "adres": "Futbol Sahası, Ürgen Paşa, 51. Sk. No:38, 31030 Antakya/Hatay",
            "mahalle": "Ürgen Paşa Mahallesi",
            "isim": "Osman Bey",
            "servis": [
                "Ulaşım"
            ],
            "telefon": "0532 212 87 97",
            "lat": 36.22423,
            "lon": 36.1556691,
            "notlar": "Her gün 13.00-14.00 saatleri arasında Antalya'ya gidecek otobüsler kalkmaktadır"
        }
    ],
    "headers": null
}
```

### /set_service_point
```zsh
$ curl --location --request POST 'https://deprem-superapp-backend.herokuapp.com/set_service_point' \
--header 'Content-Type: application/json' \
--data-raw '{
  "il": "string",
  "ilce": "string",
  "adres": "string",
  "mahalle": "string",
  "isim": "string",
  "servis": [
    "string"
  ],
  "telefon": "string",
  "lat": 0,
  "lon": 0,
  "notlar": "string"
}'


>> "63e586d4f9a73164daa3e85f"  // ObjectId of the inserted data
```

# Lisans
[GNU](LICENSE)
