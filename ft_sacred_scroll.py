import alchemy.elements
import alchemy


def test_direct_access() -> None:
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


def test_package_access() -> None:
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    test_direct_access()
    test_package_access()

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
