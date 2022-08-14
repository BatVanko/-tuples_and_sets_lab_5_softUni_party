number_of_guests = int(input())
vip = set()
regular = set()
for _ in range(number_of_guests):
    guest = input()
    first_letter = guest[0]
    if first_letter.isdigit():
        vip.add(guest)
    else:
        regular.add(guest)
in_guests = input()
while not in_guests == "END":
    if in_guests in vip:
        vip.remove(in_guests)
    elif in_guests in regular:
        regular.remove(in_guests)
    in_guests = input()

print(len(vip) + len(regular))
[print(g) for g in sorted(vip)]
[print(g) for g in sorted(regular)]




