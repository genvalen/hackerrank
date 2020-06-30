# Original problem: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
if __name__ == '__main__':
    def get_attr_number(node):
    
    score = 0
    for elem in node.iter('*'):
        if elem.attrib:
            score += len(elem.attrib)
    return(score)
