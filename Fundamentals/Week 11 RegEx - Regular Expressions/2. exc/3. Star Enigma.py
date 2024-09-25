import re

n = int(input())

attacked_planets = []
destroyed_planets = []

pattern = r"@(?P<planet>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<type>A|D)![^@\-!:>]*->(?P<soldiers>\d+)"

for _ in range(n):
    encrypted_message = input()

    key = sum(encrypted_message.lower().count(c) for c in "star")

    decrypted_message = "".join(chr(ord(char) - key) for char in encrypted_message)

    match = re.search(pattern, decrypted_message)

    if match:
        planet = match.group("planet")
        population = int(match.group("population"))
        attack_type = match.group("type")
        soldiers = int(match.group("soldiers"))

        if attack_type == "A":
            attacked_planets.append(planet)
        elif attack_type == "D":
            destroyed_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
