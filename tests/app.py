from tests.blog import Blog
from tests.post import Post

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
POST_TEMPLATE = '''
--- {} ---

{}

'''

blogs = dict() #blog_name : Blog object
posts = dict()

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    #print the available blogs
    for key, blog in blogs.items(): #(blog_name, blog), (blog_name, blog)
        print('- {}'.format(blog))

def ask_create_blog():
    title = input("Enter the title of the blog: ")
    author = input("Enter your name: ")
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input("Enter the blog title you want to read: ")

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("Enter the blog title you want to write a post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your post content: ")
    blogs[blog_name].create_post(title, content)

