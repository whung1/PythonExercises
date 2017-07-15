import json

party_list = []


class Node(object):
    def __init__(self, p):
        self.val = p['party-animal-score']
        self.name = p['name']
        self.children = []
        self.sum = None
        self.inclusive = None

    def add_child(self, child):
        self.children.append(child)

    def is_inclusive(self):
        """
        Wrapper function to return whether this node should be included while ensuring calculation if necessary
        :return: Boolean
        """
        if self.inclusive is None:
            self.__init_memoization()
        return self.inclusive

    def get_sum(self):
        """
        Wrapper function to return whether this node should be included while ensuring calculation if necessary
        :return: int
        """
        if self.sum is None:
            self.__init_memoization()
        return self.sum

    def get_grandchildren(self):
        """
        Returns list of grandchildren to this node
        :rtype: List
        """
        grandchildren = []
        if self.children is not None:
            for child in self.children:
                grandchildren.extend(child.children)
        return grandchildren

    def __init_memoization(self):
        """
        Private helper function to calculate the best way to sum party_animal_score
        for the first time
        :rtype: List
        """
        exclusive = self.__get_exclusive_sum()
        inclusive = self.__get_inclusive_sum()
        self.sum = max(exclusive, inclusive)
        self.inclusive = True if inclusive > exclusive else False

    def __get_inclusive_sum(self):
        """
        Party_animal_score summation method while including this node's val
        :return:
        """
        inclusive = self.val
        # Inclusive sum means skipping children directly to grandchildren
        for grandchild in self.get_grandchildren():
            inclusive += grandchild.get_sum()
        return inclusive

    def __get_exclusive_sum(self):
        """
        Party_animal_score summation method without including this node's val
        :return:
        """
        exclusive_sum = 0
        for child in self.children:
            exclusive_sum += child.get_sum()
        return exclusive_sum


def populate_party_list(n):
    if n is None:
        return
    if n.val > 0 and n.is_inclusive():
        party_list.append(n.name)
        for grandchild in n.get_grandchildren():
            populate_party_list(grandchild)
    else:
        for child in n.children:
            populate_party_list(child)


if __name__ == '__main__':
    print('Input JSON Filepath:')
    with open(input(), 'r') as f:
        company_list = json.load(f)

        # Create tree of subordinate children to bosses
        root = None
        nodes = dict((p['name'], Node(p)) for p in company_list)
        for p in company_list:
            if p['boss'] is not None:
                nodes[p['boss']].add_child(nodes[p['name']])
            else:  # has no boss = is CEO
                root = nodes[p['name']]

        # Max party-animal-score
        populate_party_list(root)
        print('Party List: {0}'.format(party_list))

        # CEO Required
        party_list = []
        root.inclusive = True  # To get required CEO, just ensure they are included by setting flag
        populate_party_list(root)
        print('Party List (CEO Required): {0}'.format(party_list))
