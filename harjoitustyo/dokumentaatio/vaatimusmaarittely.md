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

* Kirjautuminen
  * Voi kirjautua käyttäjänimellä tai luoda uuden käyttäjän
  * Käyttäjänimen täytyy olla vähintään 4 merkkiä ja uniikki
* Päävalikko
  * Aloita peli painike
  * Asetukset painike
  * Peliohjeet painike
  * Tulostaulu painike
* Asetukset
  * Takaisin päävalikkoon painike
  * Vaikeusasteen vaihtaminen: HELPPO, NORMAALI, VAIKEA
    * Vaikeuaste vaikuttaa madon nopeuteen
  * Madon, omenan ja pelikentän värinvaihto painikkeet
* Peliohjeet
  * Takaisin päävalikkoon painike 
  * Yksinkertaiset ohjeet kuinka peliä pelataan
* Tulostaulu
  * Takaisin päävalikkoon painike
  * Pelaajan parhaat pisteet, kaikenkaikkiaan saadut pisteet sekä peliä pelattu aika
  * Parhaiden kymmenen pelaajan pisteet
* Peli
  * Pelikenttä
    * Mato liikkuu pelikentällä
    * Peli loppuu madon osuessa reunaan
  * Mato
    * Mato liikkuu jatkuvasti
    * Matoa ohjataan nuolinäppäimillä pelin aikana
    * Peli loppuu madon osuessa itseensä
    * Madon koko kasvaa syödessään omenoita
  * Omena
    * Pelikentällä on jatkuvasti yksi omena
    * Madon syödessä omenan, uusi omena luodaan satunnaiseen paikkaan pelikentällä
    * Omenaa ei voida luoda madon päälle
    * Pelaaja saa pisteen, kun mato syö omenan
    * Pelaaja voittaa pelin, mikäli omenan syötyään mato peittää koko pelikentän
  * Pelin päättyessä
    * Pelaajan pisteet sekä pelissä kulunut aika tallennetaan
    * Pelaaja pystyy aloittamaan uuden pelin tai palaamaan päävalikkoon

## Jatkokehitysideoita
Perusversion jälkeen peliä täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
* Äänieffektit, kun omena syödään, pelin loppuessa sekä painikkeita painaessa
* Erilaisia pelikenttiä