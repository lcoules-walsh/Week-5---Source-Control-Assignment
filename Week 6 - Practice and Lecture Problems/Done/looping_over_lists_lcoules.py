# Looping Over Lists Demo lcoules

list_of_chores = [
    "Wash Dishes",
    "Vacuum Carpets",
    "Fold Laundry",
    "Unthaw Chicken"
]

for chore in list_of_chores[:3]:
    chore = chore + " (10 minutes)"
    print(chore + " Done!")