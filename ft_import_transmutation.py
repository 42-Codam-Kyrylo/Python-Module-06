def full_module():
    import alchemy.elements

    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def specific_function():
    from alchemy.elements import create_water

    print(f"create_water(): {create_water()}")


def aliased():
    from alchemy.potions import healing_potion as heal

    print(f"heal(): {heal()}")


def multiple():
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion

    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    full_module()
    print("\nMethod 2 - Specific function import:")
    specific_function()
    print("\nMethod 3 - Aliased import:")
    aliased()
    print("\nMethod 4 - Multiple imports:")
    multiple()

    print("\nAll import transmutation methods mastered!")
