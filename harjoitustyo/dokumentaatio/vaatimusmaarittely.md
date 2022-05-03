# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on toteutus [matopelistä](https://fi.wikipedia.org/wiki/Matopeli).
Pelissä ohjataan matoa, joka kuolee törmätessään itseensä tai pelikentän laitoihin.
Matoa kasvatetaan syömällä pelikentältä löytyviä omenoita,
ja pelin voi voittaa kasvattamalla madon koko pelikentän kokoiseksi

## Käyttöliittymäluonnos
Sovellus koostuu kuudesta eri näkymästä
* 1 Kirjautuminen
  * Sovellus avautuu ensiksi tänne. Sisältää nimikentän sekä kirjautusmisnapin
* 2 Päävalikko
  * Kirjautumisen jälkeen näytetään päävalikko, jossa on painikkeet on aloita peli, asetukset, peliohjeet ja tulostaulu
  * 3 Asetukset
    * Sisältää painikkeet takaisin päävalikkoon, vaikeusasteen vaihtamiseen, sekä madon, omenan ja kentän värin vaihtamiseen
  * 4 Peliohjeet
    * Sisältää peliohjeet sekä painikkeen takaisin päävalikkoon
  * 5 Tulostaulu
    * Sisältää parhaat kymmenen tulosta sekä painikkeen takaisin päävalikkoon
* 6 Pelikenttä
  * Sisältää itse pelikentän

## Perusversion tarjoama toiminnallisuus

#### Tekemättä
* Viilauksia itse peliin
* Käyttöliittymmästä hienompi

<br>
  
* Kirjautuminen | TEHTY
  * Voi kirjautua käyttäjänimellä tai luoda uuden käyttäjän | TEHTY
  * Käyttäjänimen täytyy olla vähintään 4 merkkiä ja uniikki | TEHTY
* Päävalikko | TEHTY
  * Aloita peli painike | TEHTY
  * Asetukset painike | TEHTY
  * Peliohjeet painike | TEHTY
  * Tulostaulu painike | TEHTY
* Asetukset | TEHTY
  * Takaisin päävalikkoon painike | TEHTY
  * Vaikeusasteen vaihtaminen: HELPPO, NORMAALI, VAIKEA | TEHTY
    * Vaikeuaste vaikuttaa madon nopeuteen | TEHTY
  * Madon, omenan ja pelikentän värinvaihto painikkeet | TEHTY
* Peliohjeet
  * Takaisin päävalikkoon painike | TEHTY
  * Yksinkertaiset ohjeet kuinka peliä pelataan
* Tulostaulu
  * Takaisin päävalikkoon painike | TEHTY
  * Pelaajan parhaat pisteet, kaikenkaikkiaan saadut pisteet sekä peliä pelattu aika | TEHTY
  * Parhaiden kolmen pelaajan pisteet | TEHTY
* Peli
  * Pelikenttä | TEHTY
    * Mato liikkuu pelikentällä | TEHTY
    * Peli loppuu madon osuessa reunaan | TEHTY
  * Mato | TEHTY
    * Mato liikkuu jatkuvasti | TEHTY
    * Matoa ohjataan nuolinäppäimillä pelin aikana | TEHTY
    * Peli loppuu madon osuessa itseensä | TEHTY
    * Madon koko kasvaa syödessään omenoita | TEHTY
  * Omena
    * Pelikentällä on jatkuvasti yksi omena | TEHTY
    * Madon syödessä omenan, uusi omena luodaan satunnaiseen paikkaan pelikentällä | TEHTY
    * Pelaaja saa pisteen, kun mato syö omenan | TEHTY
    * Omenaa ei voida luoda madon päälle
  * Pelin päättyessä | TEHTY
    * Pelaajan pisteet sekä pelissä kulunut aika tallennetaan | TEHTY
    * Pelaaja pystyy aloittamaan uuden pelin tai palaamaan päävalikkoon | TEHTY

## Jatkokehitysideoita
Perusversion jälkeen peliä täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
* Äänieffektit, kun omena syödään, pelin loppuessa sekä painikkeita painaessa
* Erilaisia pelikenttiä
