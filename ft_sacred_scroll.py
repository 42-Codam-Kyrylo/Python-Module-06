from collections.abc import Callable
import alchemy.elements
import alchemy


def test_direct_module_access(func: Callable[[], str]):
    print(f"{func}: {func()}")


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    direct_modules: list[Callable[[], str]] = [
        alchemy.elements.create_fire,
        alchemy.elements.create_water,
        alchemy.elements.create_earth,
        alchemy.elements.create_air,
    ]

    for direct in direct_modules:
        test_direct_module_access(direct)
