## Tehtävä 1: Monopoli

Monopolia pelataan käyttäen kahta noppaa. 
Pelaajia on vähintään 2 ja enintään 8. 
Peliä pelataan pelilaudalla joita on yksi. 
Pelilauta sisältää 40 ruutua. 
Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. 
Kullakin pelaajalla on yksi pelinappula. 
Pelinappula sijaitsee aina yhdessä ruudussa.

```mermaid
classDiagram
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "2" Noppa
    Monopoli "1" -- "2-8" Pelaaja
    Pelilauta "1" -- "40" Peliruutu
    Peliruutu "1" -- "1" Peliruutu : Seuraava ruutu
    Pelinappula "1" -- "1" Peliruutu
    Pelinappula "1" -- "1" Pelaaja
    class Monopoli { }
    class Noppa { }
    class Pelaaja { }
    class Pelilauta { }
    class Peliruutu { }
    class Pelinappula { }
```

## Tehtävä 2: Laajennettu Monopoli

Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.
Jokaiseen ruutuun liittyy jokin toiminto.
Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.
Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.
Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. 
Kadun voi omistaa joku pelaajista. 
Pelaajilla on rahaa.

```mermaid
classDiagram
    Monopoli "1" -- "1" Pelilauta
    Monopoli "1" -- "2" Noppa
    Monopoli "1" -- "2-8" Pelaaja
    
    Pelilauta "1" -- "40" Peliruutu
    Pelilauta --> Aloitusruutu
    Pelilauta --> Vankilaruutu
    
    Peliruutu "1" -- "1" Peliruutu : Seuraava ruutu
    
    Pelinappula "1" -- "1" Peliruutu
    Pelinappula "1" -- "1" Pelaaja
    
    Aloitusruutu --|> Peliruutu
    Vankilaruutu --|> Peliruutu
    Sattumaruutu --|> Peliruutu
    Yhteismaaruutu --|> Peliruutu
    Asemaruutu --|> Peliruutu
    Katuruutu --|> Peliruutu
    
    Peliruutu "1" -- "*" Toiminto
    
    Kortti "1" -- "1" Toiminto
    Sattumaruutu "1" -- "*" Kortti
    Yhteismaaruutu "1" -- "*" Kortti
    
    Katuruutu "1" -- "0-4" Talo
    Katuruutu "1" -- "1" Hotelli
    Katuruutu "1" -- "1" Pelaaja
    
    Pelaaja "1" -- "1" Tili
    
    class Monopoli { }
    class Noppa { }
    class Pelaaja { }
    class Pelilauta { }
    class Peliruutu { }
    class Pelinappula { }
    
    class Aloitusruutu { }
    class Vankilaruutu { }
    class Sattumaruutu { }
    class Yhteismaaruutu { }
    class Asemaruutu { }
    class Katuruutu {
        nimi : string
    }
    class Toiminto { }
    class Kortti { }
    
    class Talo { }
    class Hotelli { }
    
    class Tili { }
    
```