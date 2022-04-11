# Matopeli
Sovelluksella pystyy pelaamaan [matopeliä](https://fi.wikipedia.org/wiki/Matopeli).
Sovellusta voi käyttää vain yksi pelaaja kerrallaan.

## Dokumentaatio

- [Vaatimusmäärittely](harjoitustyo/dokumentaatio/vaatimusmaarittely.md)  
- [Tuntikirjanpito](harjoitustyo/dokumentaatio/tuntikirjanpito.md)
- [Changelog](harjoitustyo/dokumentaatio/changelog.md)

## Asennus

1. Kloonaa repo
2. Siirry terminaalissa kansioon ``harjoitustyo/``
3. Asenna riippuvuudet ``poetry install``
4. Käynnistä sovellus ``poetry run invoke start``

## Komentorivitoiminnot

### Ohjelman suorittaminen
Komento: ``poetry run invoke start``

### Testaus
Komento: ``poetry run invoke test``

### Testikattavuus
Komento: ``poetry run invoke coverage-report``

### Pylint
Komento: ``poetry run invoke lint``