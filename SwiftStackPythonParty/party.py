import json


class EmployeeNode:
    def __init__(self, p):
        self.val = p['party-animal-score']
        self.name = p['name']
        self.children = []
        self.sum = None
        self.inclusive = None  # Boolean flag on whether this node is better with inclusive sum

    def add_child(self, child):
        self.children.append(child)

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

    def __init_memoization(self):
        """
        Private helper function to calculate the best way to sum party_animal_score
        for the first time and whether this node is better off with inclusive sum or not
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
        Party_animal_score summation method excluding this node's val
        :return:
        """
        exclusive_sum = 0
        for child in self.children:
            exclusive_sum += child.get_sum()
        return exclusive_sum


class EmployeeTree:
    """
    Representation of the employees at a place where nodes' parents are bosses, and children
    are subordinates.
    """
    def __init__(self, employee_list):
        """
        Create tree of subordinates to bosses
        :param employee_list: list of dicts of keys 'name', 'boss', 'party-animal-score' (See sample.json)
        """
        self.root = None
        self.party_list = []
        # Populate Tree with Nodes
        nodes = dict((p['name'], EmployeeNode(p)) for p in employee_list)
        for p in employee_list:
            if p['boss'] is not None:
                nodes[p['boss']].add_child(nodes[p['name']])
            else:  # has no boss = is root / CEO
                self.root = nodes[p['name']]

    def get_party_list(self, ceo_required=False):
        """
        :param ceo_required: True if CEO is required in invite party list, False otherwise
        :return: List of invited members to party maximizing party-animal-score
        """
        self.party_list = []
        if self.root is not None:
            if ceo_required:
                self.root.inclusive = True  # To get required CEO, just ensure they are included by flag
            else:
                self.root.inclusive = None  # In case we need to reset flag on subsequent usage
            # TODO(wilson): change return to something more functional paradigm-esque while ensuring tail recursion
            self.__populate_party_list(self.root)
        return self.party_list

    def __populate_party_list(self, n):
        if n is None:
            return
        if n.val > 0 and n.is_inclusive():
            self.party_list.append(n.name)
            for grandchild in n.get_grandchildren():
                self.__populate_party_list(grandchild)
        else:
            for child in n.children:
                self.__populate_party_list(child)


if __name__ == '__main__':
    print('Input JSON Filepath:')
    with open(input(), 'r') as f:
        employee_tree = EmployeeTree(json.load(f))

        # Max party-animal-score
        print('Party Invite List: {0}'.format(employee_tree.get_party_list()))

        # CEO Required
        print('Party Invite List (CEO Required): {0}'.format(employee_tree.get_party_list(ceo_required=True)))
