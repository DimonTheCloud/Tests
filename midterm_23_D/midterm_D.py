from fontTools.misc.bezierTools import lineLineIntersections

POKEDEX = ["Bulbasaur", "Charmander", "Squirtle"]

FAST_ATTACK_NAMES = [
    ["Vine Whip", "Tackle"],
    ["Ember", "Scratch"],
    ["Tackle", "Bubble"],
]
FAST_ATTACK_STATS = [
    [(7, 6, 0.6), (5, 5, 0.5)],
    [(10, 10, 1), (6, 4, 0.5)],
    [(5, 5, 0.5), (12, 14, 1.2)],
]

CHARGED_ATTACK_NAMES = [
    ["Seed Bomb", "Sludge Bomb", "Power Whip"],
    ["Flamethrower", "Flame Charge", "Flame Burst"],
    ["Aqua Jet", "Aqua Tail", "Water Pulse"],
]
CHARGED_ATTACK_STATS = [
    [(55, 33, 2.1), (80, 50, 2.3), (90, 50, 2.6)],
    [(70, 50, 2.2), (70, 33, 3.8), (70, 50, 2.6)],
    [(45, 33, 2.6), (50, 33, 1.9), (70, 50, 3.2)],
]


def get_attack_stats(pokemon_name, attack_name, attack_name_list, attack_stats_list):
    pokemon_index = POKEDEX.index(pokemon_name)
    pokemon_attacks = attack_name_list[pokemon_index]
    attack_index = pokemon_attacks.index(attack_name)
    attack_stats = attack_stats_list[pokemon_index][attack_index]

    return attack_stats


def get_dps(pokemon_name, fast_attack_name, charged_attack_name, duration = 100):

    used_attacks = []
    energy = 0
    time = 0
    total_damage = 0

    fast_damage, fast_energy, fast_time = get_attack_stats(pokemon_name, fast_attack_name, FAST_ATTACK_NAMES, FAST_ATTACK_STATS)
    charged_damage, charged_energy, charged_time = get_attack_stats(pokemon_name, charged_attack_name, CHARGED_ATTACK_NAMES, CHARGED_ATTACK_STATS)

    while time < duration:
        if energy >= charged_energy:
            used_attacks.append(charged_attack_name)
            energy -= charged_energy
            total_damage += charged_damage
            time += charged_time

        else:
            used_attacks.append(fast_attack_name)
            energy += fast_energy
            total_damage += fast_damage
            time += fast_time

    dps = total_damage / duration
    return used_attacks, dps



def get_best_attacks(pokemon_name, fast_attack_names, charged_attack_names):
    best_dps = -1
    best_fast = None
    best_charged = None

    for fast_attack in fast_attack_names:
        for charged_attack in charged_attack_names:
            used_attacks, dps = get_dps(pokemon_name, fast_attack, charged_attack, duration = 100)

            if dps > best_dps:
                best_dps = dps
                best_fast = fast_attack
                best_charged = charged_attack

    return best_dps, best_fast, best_charged


def main(pokemons):
    result = []

    for pokemon_name, fast_attack, charged_attack in pokemons:
        pokemon_index = POKEDEX.index(pokemon_name)
        fast_attack_names = FAST_ATTACK_NAMES[pokemon_index]
        charged_attack_names = CHARGED_ATTACK_NAMES[pokemon_index]

        used_attacks, current_dps = get_dps(pokemon_name, fast_attack, charged_attack, duration=100)
        best_dps, best_fast, best_charged = get_best_attacks(
            pokemon_name, fast_attack_names, charged_attack_names
        )

        is_best = (fast_attack == best_fast and charged_attack == best_charged)
        dps_difference = best_dps - current_dps

        result.append((pokemon_name, best_fast, best_charged, is_best, dps_difference))

    return result










if __name__ == "__main__":
    pokemons = [
        ("Bulbasaur", "Vine Whip", "Seed Bomb"),
        ("Charmander", "Ember", "Flame Charge"),
        ("Squirtle", "Tackle", "Aqua Jet")
    ]

