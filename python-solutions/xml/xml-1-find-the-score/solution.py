# Original problem: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = 0
    for elem in node.iter('*'):
        if elem.attrib:
            score += len(elem.attrib)

    return(score)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
