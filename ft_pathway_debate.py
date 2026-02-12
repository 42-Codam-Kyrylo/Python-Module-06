def absolute():
    import alchemy.transmutation.basic as absolute

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {absolute.lead_to_gold()}")
    print(f"stone_to_gem(): {absolute.stone_to_gem()}")


def relative():
    import alchemy.transmutation.advanced as advanced_mod

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): " f"{advanced_mod.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced_mod.elixir_of_life()}")


def package_access():
    import alchemy.transmutation

    print("\nTesting Package Access:")
    name = "alchemy.transmutation.lead_to_gold():"
    print(f"{name} {alchemy.transmutation.lead_to_gold()}")
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    absolute()
    relative()
    package_access()

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
