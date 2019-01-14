import mlab

from models.user import User
from models.post import Post
mlab.connect()

# a_random_user = User.objects(username = "anhson").first()
# if a_random_user is None:
#     print("User not found")
# else:
#     new_post = Post(title = "Bai viet  @@@",
#                     content = "alo dag dau day",
#                     owner = a_random_user)
#     new_post.save()
#     print("Done saving...")

# thop 1 : Post =) Owner
# for post in Post.objects():
#     print(post.title,"by",post.owner.username)
    

# thop 2 : Owner =) Posts
user = User.objects(username = "anhson").first()
posts = Post.objects(owner = user)
for post in posts:
    print(post.title)