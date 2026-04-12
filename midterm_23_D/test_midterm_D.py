import pytest

from midterm_D import (
    POKEDEX,
    FAST_ATTACK_NAMES,
    FAST_ATTACK_STATS,
    CHARGED_ATTACK_NAMES,
    CHARGED_ATTACK_STATS,
    get_attack_stats,
    get_dps,
    get_best_attacks,
    main,
)


def test_get_attack_stats_fast():
    assert get_attack_stats(
        "Bulbasaur",
        "Vine Whip",
        FAST_ATTACK_NAMES,
        FAST_ATTACK_STATS
    ) == (7, 6, 0.6)


def test_get_attack_stats_charged():
    assert get_attack_stats(
        "Charmander",
        "Flame Charge",
        CHARGED_ATTACK_NAMES,
        CHARGED_ATTACK_STATS
    ) == (70, 33, 3.8)


def test_get_dps_returns_correct_types():
    used_attacks, dps = get_dps("Bulbasaur", "Vine Whip", "Seed Bomb", duration=10)

    assert isinstance(used_attacks, list)
    assert isinstance(dps, float)
    assert len(used_attacks) > 0
    assert dps > 0


def test_get_dps_uses_only_selected_attacks():
    used_attacks, dps = get_dps("Squirtle", "Bubble", "Aqua Tail", duration=20)

    assert dps > 0
    assert set(used_attacks).issubset({"Bubble", "Aqua Tail"})


def test_get_dps_can_use_charged_attack():
    used_attacks, dps = get_dps("Charmander", "Ember", "Flame Charge", duration=20)

    assert "Flame Charge" in used_attacks


def test_get_best_attacks_returns_valid_combination():
    best_dps, best_fast, best_charged = get_best_attacks(
        "Bulbasaur",
        FAST_ATTACK_NAMES[0],
        CHARGED_ATTACK_NAMES[0]
    )

    assert isinstance(best_dps, float)
    assert best_fast in FAST_ATTACK_NAMES[0]
    assert best_charged in CHARGED_ATTACK_NAMES[0]
    assert best_dps > 0


def test_get_best_attacks_is_really_best_for_bulbasaur():
    best_dps, best_fast, best_charged = get_best_attacks(
        "Bulbasaur",
        FAST_ATTACK_NAMES[0],
        CHARGED_ATTACK_NAMES[0]
    )

    all_results = []
    for fast_attack in FAST_ATTACK_NAMES[0]:
        for charged_attack in CHARGED_ATTACK_NAMES[0]:
            _, dps = get_dps("Bulbasaur", fast_attack, charged_attack, duration=100)
            all_results.append((dps, fast_attack, charged_attack))

    expected_best_dps, expected_best_fast, expected_best_charged = max(all_results, key=lambda x: x[0])

    assert best_dps == expected_best_dps
    assert best_fast == expected_best_fast
    assert best_charged == expected_best_charged


def test_main_returns_correct_structure():
    pokemons = [
        ("Bulbasaur", "Vine Whip", "Seed Bomb"),
        ("Charmander", "Ember", "Flame Charge"),
        ("Squirtle", "Tackle", "Aqua Jet"),
    ]

    result = main(pokemons)

    assert isinstance(result, list)
    assert len(result) == 3

    for item in result:
        assert isinstance(item, tuple)
        assert len(item) == 5

        pokemon_name, best_fast, best_charged, is_best, dps_difference = item

        assert pokemon_name in POKEDEX
        assert isinstance(best_fast, str)
        assert isinstance(best_charged, str)
        assert isinstance(is_best, bool)
        assert isinstance(dps_difference, (int, float))


def test_main_best_flag_matches_attacks():
    pokemons = [
        ("Bulbasaur", "Vine Whip", "Seed Bomb"),
    ]

    result = main(pokemons)
    pokemon_name, best_fast, best_charged, is_best, dps_difference = result[0]

    expected_is_best = ("Vine Whip" == best_fast and "Seed Bomb" == best_charged)
    assert is_best == expected_is_best


def test_main_difference_is_non_negative():
    pokemons = [
        ("Bulbasaur", "Vine Whip", "Seed Bomb"),
        ("Charmander", "Scratch", "Flamethrower"),
        ("Squirtle", "Bubble", "Water Pulse"),
    ]

    result = main(pokemons)

    for item in result:
        assert item[4] >= 0