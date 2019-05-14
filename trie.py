# Implementing a Trie to Store a Series of Small Nucleotide Sequences/Fragments
#    ---for easy probing of large target sequence----

# Pavithra
# May 13, 2019
# With credit to Miguel Rocha, Pedro G. Ferreira - Bioinformatics Algorithms: Design and Implementation in Python - Ch. 16.2
# This is my version, with my small personal modifications to the code, added functions, and extensive commenting!


class Trie:

    """ELEMENTARY FUNCTIONS"""
    ###########################################

    def __init__(self):

        self.nodes = {0: {}}  # Essentially, is a dictionary of dictionaries
        self.size = 0  # Keeps track of the # of nodes in the trie.

    def print_trie(self):
        for key in self.nodes:
            print(key, "->", self.nodes[key])  # Each nucleotide character points to a 'future' character position.

    def add_edge_to_trie(self, path_key, nucleotide):
        # Adds a SINGLE nucleotide character to the trie, GIVEN THE POSITION it must FOLLOW AFTER.
        # Example: Suppose ATC exists in trie.
        # I have a sequence ATCA so I wish to add A after the C.
        # Given the key value of the node that C points to...i.e. 3, then this will add C to node 3 in the trie.
        self.size += 1
        self.nodes[path_key][nucleotide] = self.size  # This character must point to the next 'future' character position.
        self.nodes[self.size] = {}  # No future characters exist yet.

    def get_position(self, sequence):
        # Returns the position of the LAST letter of a given SUBSEQUENCE THAT EXISTS IN the trie.
                # If sequence does not exist, does not do anything.
        # Example: CCA is the prefix, and it is present in the trie. A, the edge, points to node 4.
        # Returns: 4
        (m, pos) = self.search_exact_prefix(sequence)
        if m == sequence:
            return(pos)

    def add_sequence(self, seq):
        # Add the sequence to the trie.
        path = 0  # keeps track of the path we are currently on
        for letter in seq:
            if letter not in self.nodes[path]:  # if the letter is not found on this path
                self.add_edge_to_trie(path, letter)  # add an edge
            path = self.nodes[path][letter]  # need to reupdate path to go down the trie depth_wise, and not be stuck breadth_wise.

    def make_trie(self, patterns):
        # Given a LIST of sequences, converts sequence into a trie.
        for i in patterns:
            self.add_sequence(i)
    ############################################

    def search_exact_prefix(self, sequence):
        # Finds a SUBSEQUENCE/SEQUENCE of the provided sequence in the trie (IF IT EXISTS of course),
                # and returns the prefix found, as well as the node position that the LAST LETTER of the FOUND SUBSEQUENCE points to.
        # Example: I want to find whether a prefix of "AGTGCA" exists in the trie.
        # ('AGT', 10)
                # This means that the prefix 'AGT' is in the trie and the letter T in AGT pattern points to the node 10.
        path = 0
        match = ""
        for letter in sequence:
            if letter in self.nodes[path]:
                match += letter
            else:  # cannot search depth-wise any more. The path ends here!
                return (match, path)
            path = self.nodes[path][letter]
        return (match, path)

    def all_subsequence_matches(self, sequence):
        # Finds ALL matches of the SUBSEQUENCES of a sequence.
        # So for a given sequence: GAAATGA
        # This will search and check whether GAAATGA, AAATGA, AATGA...and so on exists in the trie or not.
        matches = set()
        for i in range(len(sequence)):
            (m, path) = self.search_exact_prefix(sequence[i:])
            if m != "":
                matches.add(m)
        return list(matches)


def main():
    t = Trie()
    patterns = ["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"]
    t.make_trie(patterns)
    print (t.search_exact_prefix("GAGATCCTA"))
    print (t.all_subsequence_matches("GAGATCCTA"))
    t.print_trie()
    position = t.get_position("AGC")
    t.add_edge_to_trie(position, "U")
    t.print_trie()


main()
