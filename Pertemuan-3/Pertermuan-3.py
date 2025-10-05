from bs4 import BeautifulSoup

#P3.1
# html = "<div>Hello World</div>"
# soup = BeautifulSoup(html, "html.parser")
# print(soup.p.text)

#P3.2
# html = """
# <div>This is a div</div>
# <p>This is a paragraph</p>
# <p>This is another paragraph</p>
# """
# soup = BeautifulSoup(html, "html.parser")
# print(soup.div.text)
# print(soup.find_all("p"))
# print(soup.find_all("div")[1])

# P3.3
# html = """
# <div>This is a div</div>
# <p>This is a paragraph</p>
# <div class="test">This is a div with a class</div>
# <p>This is another paragraph</p>
# """
# soup = BeautifulSoup(html, "html.parser")
# print(soup.find_all(class_="test"))

# Literally you can't find ID because it was never defined
# print(soup.find_all("P", id="first"))

# P3.4
# html = """
# <div id="d1" class="wide">
#     <p>This is a paragraph</p>
#     <img src="image.jpg" id="img1">
#     <p>This is another paragraph</p>
#     <a href="https://www.google.com">Google</a>
# </div>
# <div id="d2" class="small">
#     <p>This is a paragraph</p>
#     <img src="image.jpg" id="img2">
#     <p>This is another paragraph</p>
#     <a href="https://www.google.com">Google</a>
# </div>
# <div class="test">This is a div with a class</div>
# <p>This is another paragraph</p>
# """
# soup = BeautifulSoup(html, "html.parser")
# divs = soup.find_all('div', {'id': 'd1'})
# print(divs[0].p.text)

# P3.5
# html = """
#     <div id="d1" class="wide">
#         <p id='p1'>This is a paragraph</p>
#         <div><p>OK</p></div>
#         <img src="image.jpg" id="img1">
#         <a href="https://www.google.com">Google</a>
#     </div>
#         <div id="d1" class="small">
#         <p id='p1'>This is a paragraph</p>
#         <div><p>KO</p></div>
#         <img src="image.jpg" id="img2">
#         <a href="https://www.google.com">Google</a>
#     </div>-
# """
# soup = BeautifulSoup(html, "html.parser")
# divs = soup.find_all("div", {"id": "d1"})[1].div.p.text
# print(divs)

#P3.6
html4 = """
    <div>div1</div>
    <div>div2</div>
    <div>div3</div>
    <div>div4</div>
    <div>div5</div>
    <div>div6</div>
    <div>div7</div>
    <div>div8</div>
    <div>div9</div>
    <div>div10</div>
"""
soup = BeautifulSoup(html4, "html.parser")



all_divs_2 = soup.find_all("div")
divs = [div.text for i, div in enumerate(all_divs_2) if i % 2 == 0]
print(divs)
