# python3
import sys
from collections import defaultdict

class Node:
	def __init__ (self):
		self.children = {}
		self.patternEnd = False


def _build_trie(patterns):
	tree = Node()
	for pattern in patterns:
		curr_node = tree
		for i in range(len(pattern)):
			char = pattern[i]
			if char in curr_node.children:
				curr_node = curr_node.children[char]
			else:
				newNode = Node()
				curr_node.children[char] = newNode
				curr_node = newNode
		curr_node.patternEnd = True

	return tree


def _prefix_trie_match(text, trie):
	t = trie
	index = 0
	char = text[index]
	
	while True:
		if len(t.children) == 0:
			return True
		elif char in t.children:
			t = t.children[char]
			if index < len(text) - 1:
				index += 1
				char = text[index]
			else:
				char = None
			if t.patternEnd:
				return True
		else:
			return False


def solve (text, n, patterns):
	result = []
	trie = _build_trie(patterns)
	
	for i in range(len(text)):
		if _prefix_trie_match(text[i:], trie):
			result.append(i)
	
	result = list(set(result))
	result.sort()
	return result	


if __name__ == "__main__":
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]

	ans = solve (text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
