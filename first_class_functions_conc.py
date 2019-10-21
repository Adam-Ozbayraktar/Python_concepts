# First call functions allow us to treat functions like any other object 
def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text

# Print_h1 is assigned the function wrap_text with arg tag
# print_h1 can now be used as a function

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
print_p('Hello World my name is jocker')
