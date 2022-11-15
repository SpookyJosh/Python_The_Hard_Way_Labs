states = {
"OH":"Cleveland",
"NC":"Raleigh"
}

#add some entries

states['MD'] = "Baltimore"
states['PA'] = "Pittsburgh"

print(states)

for abbrev, city in list(states.items()):
    print(f"The abbreviation is {abbrev} and the City is {city}")
