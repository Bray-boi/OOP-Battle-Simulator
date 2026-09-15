from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Ring of Champions"


def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        print(f"What does {hero.name} do?")
        print("1 Attack")
        print("2 Heal")
        print("3 Run")
        hero_action = input("")
        if hero_action == "1":
            hero_damage = hero.attack()
            enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

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
    

    print(f"{hero.name} steps into the arena with {hero.health} health and is of the {hero.race} race.")
    damage = hero.attack()
    print(f"{hero.name} leaps forward striking {goblin.name} dealing {damage} damage!")
    goblin.take_damage(damage)
    if goblin.is_alive():
        damage = goblin.attack()
        print(f"Fred hits back!")
        hero.take_damage(damage)
        hero.is_alive()

    battle(hero, goblin)
    if hero.is_alive():
        battle(hero, secondGoblin)
if __name__ == "__main__":
    main()
