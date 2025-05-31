# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an erorr that I made up.")


# height = float(input("Height : "))
# weight = int(input("Weight : "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / weight ** 2
#
# print(bmi)
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes



print(count_likes(facebook_posts))