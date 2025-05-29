class User:
    """ Constructors for initialization attributes """
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

user1 = User("001", "violet")
user2 = User("002", "thanatos")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)