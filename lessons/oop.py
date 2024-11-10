"""OOP & Classes"""


class Profile:
    # declaring attributes for an Instagram Profile
    username: str
    bio: str
    followers: int
    following: int
    private: bool

    def __init__(self):
        # initializing attributes for an Instagram Profile
        self.username = "usr9"
        self.bio = ""
        self.followers = 0
        self.following = 0
        self.private = False


my_prof: Profile = Profile()  # constructs a new Instagram profile
