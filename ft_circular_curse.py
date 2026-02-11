import alchemy.grimoire


def main():

    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    res1 = alchemy.grimoire.validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {res1}')

    res2 = alchemy.grimoire.validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {res2}\n')

    print("Testing spell recording with validation:")
    res3 = alchemy.grimoire.record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {res3}')

    res4 = alchemy.grimoire.record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {res4}\n')

    print("Testing late import technique:")
    res5 = alchemy.grimoire.record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {res5}\n')

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
