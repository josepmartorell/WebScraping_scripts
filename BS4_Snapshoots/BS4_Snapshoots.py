# import package
from bs4 import BeautifulSoup

# FIXME I: Below are bs4 tricks from udemy's course no 2, sections 7-8:
# source
def read_file():
    file = open('nautalia.html')
    data = file.read()
    file.close()
    return data


# make soup
html_file = read_file()
soup = BeautifulSoup(html_file, 'lxml')

# display code prettify vs access tag
print(soup.prettify())
'''print('\n\tSEPARATOR\n')
body = soup.body
print(body)'''

# access tag
# meta = soup.meta
# print(meta)

# access tag
# title = soup.title
# print(title)

# access tag
'''p = soup.p
print(p)

p = soup.p
print(p.contents)

p = soup.p
for child in p.contents:
    print(child)'''

# access class attribute value
# body = soup.body
# print(body['class'])

# tag.children returns an iterator: HEAD,DIV,FOOTER and 8 SCRIPT
'''body = soup.body
for child in body.children:
    print(child if child is not None else '', end='\n\nSEPARATOR\n\n')'''

# tag.contents returns us direct children of the said tag for example FOOTER in [2] position
'''body = soup.body
children = [child for child in body.contents if child != '\n']
print(children[2])
len_children =  len(children)
print('\n\tNUMBER OF CHILDREN: ' + str(len_children))'''

# todo: FIRST STEP: descendant list to select a target (tag.descendants returns us all the children of the said tag)
list_descendants = []
for index, child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '\\n')
    list_descendants.append(child)

# todo: SECOND STEP: targeting the selected target
print('\n\tTARGET: ' + list_descendants[87])

# FIXME II: Below are bs4 tricks from udemy's course no 2, sections 9-10:

# html contents
# html = soup.html
# print(html.contents)

# body contents
# body = soup.body
# print(body.contents)

# the parent of DIV tag is HEADER (check with prettify)
# parent = soup.div.parent
# print(parent)

# the parent of TITLE tag is HEAD (check with prettify)
# parent = soup.title.parent
# print(parent)

# nested parent tags from A to backwards
'''link = soup.a
for parent in link.parents:
    print(parent.name)'''

# previous sibling for BODY is HEAD
body = soup.body
print(body.previous_sibling.previous_sibling)

# .next_sibling
'''p = soup.body.p
print(p)
print(p.next_sibling.next_sibling)'''



