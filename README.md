# Kirja-arvostelut

Sovelluksessa käyttäjät voivat lisätä kirjoja ja arvostella niitä.

## Sovelluksen toiminnot

- Käyttäjä voi luoda tunnuksen ja kirjautua sisään.
- Käyttäjä voi lisätä, muokata ja poistaa kirjoja.
- Käyttäjä voi sekä selata että etsiä kirjoja hakusanoin.
- Kirjoja voi luokitella genren ja kielen mukaan.
- Käyttäjäsivulla näkyvät käyttäjän lisäämät kirjat ja tilastoja.
- Käyttäjä voi arvostella omia ja muiden lisäämiä kirjoja antamalla arvosanan ja kommentin.
- Kirjan sivulla näkyvät sen saamat arvostelut.

## Sovelluksen tilanne

Tällä hetkellä toteutettu:

- Käyttäjä voi luoda tunnuksen, kirjautua sisään ja kirjautua ulos.
- Käyttäjä voi lisätä kirjoja sekä muokata ja poistaa lisäämiään kirjoja.
- Käyttäjä näkee etusivulla kaikkien käyttäjien lisäämät kirjat ja jokaisen kirjan omalla sivullaan.
- Käyttäjä voi etsiä kirjoja hakusanalla, joka voi olla osa kirjan nimeä, kirjailijaa tai kuvausta.

Vielä toteuttamatta: kirjojen luokittelu, käyttäjäsivut ja arvostelut.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut:

```
$ sqlite3 database.db < schema.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

Sovellus on tämän jälkeen osoitteessa http://127.0.0.1:5000.

## Sovelluksen testaus

1. Luo tunnus ja kirjaudu sisään.
2. Lisää muutama kirja valikon linkistä "Uusi kirja".
3. Avaa kirjan sivu etusivulta, ja kokeile kirjan muokkaamista ja poistamista.
4. Etsi kirjoja "Etsi kirjaa" -sivulla esimerkiksi kirjailijan nimen osalla.
