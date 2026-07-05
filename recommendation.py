print(" AI Recommendation System ")

print("\nChoose your favorite category:")
print("1. Books")
print("2. Movies")
print("3. Music")
print("4. Sports")

choice = input("Enter your choice (Books/Movies/Music/Sports): ").lower()

if choice == "books":
    print("\nRecommended Books:")
    print("- Atomic Habits")
    print("- Rich Dad Poor Dad")
    print("- The Alchemist")

elif choice == "movies":
    print("\nRecommended Movies:")
    print("- 3 Idiots")
    print("- Interstellar")
    print("- The Pursuit of Happyness")

elif choice == "music":
    print("\nRecommended Music:")
    print("- Imagine Dragons")
    print("- Arijit Singh")
    print("- A. R. Rahman")

elif choice == "sports":
    print("\nRecommended Sports:")
    print("- Cricket")
    print("- Football")
    print("- Badminton")

else:
    print("\nSorry! No recommendations found.")
