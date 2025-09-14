nev = input("Kérem adja meg a nevét: ")
print(f"Üdvözlünk {nev}!")

autov=input("Kérem vlászzon ki egy autót! (BMW, Ford, Audi): ")
print(f"A választott autója: {autov}")

berles=int(input("Hány napra szeretné választott autóját bérelni?: "))

if autov == "BMW":
    összeg = 15000 * berles
    print(f"Az összeg: {összeg}")
elif autov == "Ford":
    összeg = 14000 * berles
    print(f"Az összeg: {összeg}")
elif autov == "Audi":
    összeg = 14500 * berles
    print(f"Az összeg: {összeg}")
else:
    print("Hibás adat!")

