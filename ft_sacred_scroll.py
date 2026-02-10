from collections.abc import Callable
import alchemy.elements
import alchemy


def test_direct_access():
    print("Testing direct module access:")

    elements_to_test = [
        ("alchemy.elements.create_fire()", alchemy.elements.create_fire),
        ("alchemy.elements.create_water()", alchemy.elements.create_water),
        ("alchemy.elements.create_earth()", alchemy.elements.create_earth),
        ("alchemy.elements.create_air()", alchemy.elements.create_air),
    ]

    for path, func in elements_to_test:
        try:
            print(f"{path}: {func()}")
        except AttributeError:
            print(f"{path}: AttributeError")


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    test_direct_access()
