# Problem 3-1 lcoules

books = [
    "harry potter",
    "the goldfinch",
    "shooting stars",
    "the mamba mentality"
]

print("I just read:", books[0].title())
print("I just read:", books[1].title())
print("I just read:", books[2].title())
print("I just read:", books[3].title())

# Problem 3-2

tv_shows = [
    "the boys",
    "breaking bad",
    "better call saul",
    "invincible"
]

# Replaces cancelled show
tv_shows[2] = "reacher"

# Adds shows
tv_shows.append("peaky blinders")
tv_shows.insert(2, "attack on titan")

# Removes last show
removed_show = tv_shows.pop()
print("Removed Show:", removed_show)

# Delete first three rows
del tv_shows[0]
del tv_shows[0]
del tv_shows[0]

print("Remaining shows:")
print(tv_shows)

# Problem 3-3

video_games = [
    "minecraft",
    "gta",
    "expedition 33",
    "rainbow six siege",
    "csgo"
]

# len()
print("Length of list:", len(video_games))

# sorted()
print("Temporaily sorted list:")
print(sorted(video_games))

# sort()
video_games.sort()
print("Permanently sorted list:")
print(video_games)

# reverse()
video_games.reverse()
print("Reversed list:")
print(video_games)

# Problem 3-4

numbers = [1, 2, 3]

# Causes an indexing error
# print(number[5])

# Fix
# print(number[2])