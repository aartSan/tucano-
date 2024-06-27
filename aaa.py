class Player #lightblue {
  name : str
  hand : Hand
  type : PlayerInteraction
  ==
  choose_row([Row], [Player]) -> int
  ..
  save() -> json
  load(json)
}
Player o-- PlayerInteractions

class Card #lightblue {
  KINDS : [str]
  CARD_COUNTS : {str : int}
  ..
  kind : str
  ==
  __str__() -> str
  score(str{kind}, int) -> int
  ..
  save() -> json
  load(json)
}

class Hand #lightblue{
  cards : [Card]
  ==
  __str__()
  add_cards([Card])
  score() -> int
  ..
  save() -> json
  load(json)
}
Player o-- Hand

class Row #lightblue{
  cards : [Card]
  ==
  add_card(Card)
  take_cards() -> [Cards]
  ..
  save() -> json
  load(json)
}
GameState o-- Row

class Deck #lightblue{
  cards : [Card]
  ==
  draw_card() -> Card
  shuffle()
  remaining_cards() -> int
  ..
  save() -> json
  load(json)
}
GameState o-- Deck

class GameState #lightblue {
  players : [Player]
  current_player : int
  rows : [Row]
  deck : Deck
  ==
  add_cards()
  take_row(int player, int row)
  ..
  save() -> json
  load(json)
}
GameState o-- Player
GameState o-- Card

class PlayerInteractions #pink/white {
  choose_row(Hand, [Row], [Player]) -> int
}

class Human #pink {
  choose_row(Hand, [Row], [Player]) -> int
}
Human <|-- PlayerInteractions

class AI #pink {
  choose_row(Hand, [Row], [Player]) -> int
}
AI <|-- PlayerInteractions

class GameInteractions #lightgreen {
  ==
  run()
  load(json)
  ..
  request_players() -> [Player]
  print_rows([Row])
  print_player(Player)
}
GameInteractions -- GameState
