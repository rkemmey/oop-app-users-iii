# Your User class goes here
class User:
    posts=[]
    
    def __init__(self, name, email, drivers_license):
        self.name=name
        self.email=email
        self.drivers_license=drivers_license
        self.user_posts=[]
        
        
    def create_a_post(self):
        id=len(self.posts)+1
        user_title=input("Please enter the title of your post:\n")
        user_body=input("Please enter the content of your post:\n")
        self.posts.append({"id":id,"title":user_title, "content":user_body})
        self.user_posts.append({"id":id,"title":user_title, "content":user_body})
        
        
    def delete_a_post(self):
        id=input("Please enter the ID of the post you would like to delete:\n")
        for i in range(len(self.user_posts)):
            if self.user_posts[i]['id']== id:
                self.user_posts.pop(i)
        for j in range(len(self.posts)):
            if self.posts[j]['id']==id:
                self.posts.pop(j)
                
    @classmethod
    def see_all_posts(self):
        for i in self.posts:
            print(f"Title: {i['title']}\nContent:\n{i['content']}")
        
    def see_my_posts(self):
        for i in self.user_posts:
            print(f"Title: {i['title']}\nContent:\n{i['content']}")