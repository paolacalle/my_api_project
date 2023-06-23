input_name = input("Enter Character Name: ")
name = input_name.replace(" ", "%20")

response = requests.get(f"https://api.disneyapi.dev/character?name={name}")
data = response.json()

print("------------------------------------")
print(f"\nSome films that {input_name} is in are...\n")

i = 1
for values in data['data'][1]['films']: 
  print(f"{i}: {values}\n")
  i += 1

if len(data['data'][1]['films']) == 0: 
  print(f"Could not find {input_name}")

print("-----------------------------------")
