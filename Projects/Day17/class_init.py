class User():
    
    def __init__(self, username, user_id):
        self.name = username
        self.id = user_id
        self.followers = 0
        self.following = 0
        print(f"A new user {username} with id {user_id} has being created")
    
    def follow_accout(self, user):
        user.followers += 1
        self.following += 1
        
        

user1 = User("Emmanuel", "001")
user2 = User("Emike", "002")
user3 = User("Gift", "003")

print(user1.name)
print(user2.id)

user1.follow_accout(user2)
user3.follow_accout(user2)
user3.follow_accout(user1)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)