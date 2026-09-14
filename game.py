from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Ring of Champions"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ |_(`_`)_/")
    print("The gates are opening...")

    hero = Hero("Jimminy")
    goblin = Goblin("Fred")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    secondGoblin = Goblin("Scribble")
    
    print(f"{secondGoblin.name} enters the arena with {secondGoblin.health} health.")
    print("But no hero has answered the call... yet.")

    print(f"{hero.name} steps into the arena with {hero.health} health.")
    damage = hero.attack()
    print(f"{hero.name} leaps forward striking {goblin.name} dealing {damage} damage!")
    goblin.take_damage(damage)
    if goblin.is_alive():
        damage = goblin.attack()
        print(f"Fred hits back!")
        hero.take_damage(damage)
        hero.is_alive()

if __name__ == "__main__":
    main()
