from xml.etree import ElementTree as ET


class FixmlTools(ET.ElementTree):

    def get_children_tag_if_you_have_one(self, element):
        for i in range(0, len(element.getchildren())):
            a = element.getchildren()
            if element.getchildren():
                self.tag_list.appeng(a[j].tag)
                self.get_children_tag_if_you_have_one(a[j])
            else:
                break

    def get_all_tags(self):
        self.tag_list = []
        root_element = self.element_tree.getroot()
        self.tag_list.append(root_element.tag)
        self.get_children_tag_if_you_have_one(root_element)
