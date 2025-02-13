from users.User import User

class FreeUser(User):

    def create_a_post(self):
        id=len(self.posts)+1
        if len(self.user_posts) < 2:
            user_title=input("Please enter the title of your post:\n")
            user_body=input("Please enter the content of your post:\n")
            self.posts.append({"id":id,"title":user_title, "content":user_body})
            self.user_posts.append({"id":id,"title":user_title, "content":user_body})
        else:
            print("Post exceeds post limits for free accounts.")