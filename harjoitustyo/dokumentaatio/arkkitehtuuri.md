```mermaid
classDiagram
    index "1" -- "1" UI
    UI "1" -- "1" LeaderboardView
    UI "1" -- "1" InstructionsView
    UI "1" -- "1" MainView
    UI "1" -- "1" LoginView
    UI "1" -- "1" SettingsView
    MainView "1" -- "1" SnakeGame
    SnakeGame "1" -- "1" SnakeGameLoop
```