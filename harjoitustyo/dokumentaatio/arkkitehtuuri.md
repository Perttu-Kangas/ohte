## Luokkakaavio
```mermaid
classDiagram
    UILogic "1" -- "1" LeaderboardView
    UILogic "1" -- "1" MainView
    UILogic "1" -- "1" LoginView
    UILogic "1" -- "1" SettingsView
    MainView "1" -- "1" SnakeGame
    SnakeGame "1" -- "1" GameEndView
    GameEndView "1" -- "1" MainView
    SnakeGame "1" -- "1" SnakeGameLoop
```

## Sekvenssikaavio kirjautumisesta
Oletuksena on, että tietokanta on tyhjä.

```mermaid
sequenceDiagram
	participant LoginView
	participant UILogic
	participant PlayerRepository
	participant Player
	participant Connection
	LoginView ->> UILogic: login("test")
	UILogic ->> PlayerRepository: find_by_playername("test")
	PlayerRepository ->> Connection: execute(find sql)
	Connection -->> PlayerRepository: None
	PlayerRepository -->> UILogic: None
	UILogic ->> Player: Player("test", ...)
	Player -->> UILogic: Player("test", ...)
	UILogic ->> PlayerRepository: create(Player)
	PlayerRepository ->> Connection: execute(insert sql)
	Connection -->> PlayerRepository: None
	PlayerRepository -->> UILogic: Player
```

## Sovelluslogiikka
Sovelluslogiikka on jaettu kahteen osaan. Käyttöliittymään ja peliin.
`UILogic` luokka vastaa käyttöliittymän logiikasta, ja `SnakeGame` luokka pelin logiikasta.  

Käynnistyksen yhteydessä luotu `UILogic` objekti annetaan parametrina aina `UI` luokille, joiden pitää
käyttää esimerkiksi tietokantaa. `UILogic` objektiin tallenetaan myös kirjautumisen yhteydessä
nykyinen `Player` -olio.  

`SnakeGame` luokalle annetaan `start` metodia kutsuttaessa pelinpäättymis metodi parametrina, jonka perusteella
`SnakeGame` avaa pelinpäättymisnäkymän.  

`UILogic` pääsee käsiksi `PlayerRepository` sekä `GameRepository` luokkiin, sillä sen toimivuus vaatii
kummankin käyttöoikeutta. `SnakeGame` pääsee käsiksi `GameRepository`, jotta se pystyy tallentamaan pelejä tietokantaan.

## Pakkauskaavio
```mermaid
classDiagram
    UI "1" -- "1" services
    services "1" -- "1" entities
    services "1" -- "1" repositories
    repositories "1" -- "1" entities
    class services {
        SnakeGame
        SnakeGameLoop
        UILogic
    }
    class entities {
        Apple
        Player
        Snake
    }
    class repositories {
        GameRepository
        PlayerRepository
    }
```