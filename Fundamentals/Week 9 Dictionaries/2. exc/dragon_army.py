class Dragon:
    def __init__(self, colour, name, damage, health, armor):
        self.colour = colour
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def __str__(self):
        return f"-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}"


def main():
    DEFAULT_HEALTH = 250
    DEFAULT_DAMAGE = 45
    DEFAULT_ARMOR = 10

    all_dragons = {}

    # Read the number of dragons
    number_of_dragons = int(input().strip())

    for _ in range(number_of_dragons):
        # Read and split input
        input_line = input().strip()
        parts = input_line.split()

        colour = parts[0]
        name = parts[1]
        damage = int(parts[2]) if parts[2] != 'null' else DEFAULT_DAMAGE
        health = int(parts[3]) if parts[3] != 'null' else DEFAULT_HEALTH
        armor = int(parts[4]) if parts[4] != 'null' else DEFAULT_ARMOR

        dragon = Dragon(colour, name, damage, health, armor)

        if colour not in all_dragons:
            all_dragons[colour] = []

        # Check if dragon exists and update
        existing_dragon = next((d for d in all_dragons[colour] if d.name == name), None)
        if existing_dragon:
            index = all_dragons[colour].index(existing_dragon)
            all_dragons[colour][index] = dragon
        else:
            all_dragons[colour].append(dragon)

    for colour, dragons in all_dragons.items():
        # Calculate averages
        total_damage = sum(d.damage for d in dragons) / len(dragons)
        total_health = sum(d.health for d in dragons) / len(dragons)
        total_armor = sum(d.armor for d in dragons) / len(dragons)

        # Print type average stats
        print(f"{colour}::({total_damage:.2f}/{total_health:.2f}/{total_armor:.2f})")

        # Sort dragons by name and print them
        for dragon in sorted(dragons, key=lambda d: d.name):
            print(dragon)


if __name__ == "__main__":
    main()
