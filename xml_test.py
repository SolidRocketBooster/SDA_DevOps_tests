from xml.etree import ElementTree
root = ElementTree.parse('test.xml').getroot()

Heroes = {}
for child in root:
    Heroes.setdefault(child.tag, child.attrib)
    for child_2 in child:
        Heroes[child.tag].setdefault(child_2.tag, child_2.text)

for hero in Heroes.values():
    h_class = hero['class']
    name = hero['name']
    armour = hero['armour']
    hp = hero['hp']
    print(f'Class: {h_class}, Name: {name}, HP: {hp}, Armour: {armour}')

