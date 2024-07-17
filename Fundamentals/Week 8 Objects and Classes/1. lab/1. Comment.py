
class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# u_name = input()
# u_content = input()
# u_likes = input()
# comment = Comment(u_name, u_content, u_likes)
comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


# # user1
# # I like this book
# # 0
