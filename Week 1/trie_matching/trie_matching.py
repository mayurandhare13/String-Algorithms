# python3
import sys

def _build_trie(patterns):
	tree = dict()
	tree[0] = {}
	index = 1

	for pattern in patterns:
		curr_node = tree[0]
		for char in pattern:
			if char in curr_node:
				curr_node = tree[curr_node[char]]
			else:
				curr_node[char] = index
				tree[index] = {}
				curr_node = tree[index]
				index += 1

	return tree


def _prefix_trie_matching(text, trie):
	index = 0
	char = text[index]
	curr_node = trie[0]

	while True:
		if not curr_node:	#reach the leaf node
			return True
		elif char in curr_node:
			curr_node = trie[curr_node[char]]
			index += 1
			if index < len(text):
				char = text[index]
			else:
				char = '$'
		else:
			return False


def solve (text, n, patterns):
	result = []
	trie = _build_trie(patterns)

	for i in range(len(text)):
		if _prefix_trie_matching(text[i:], trie):
			result.append(i)

	return result


if __name__ == "__main__":
	text = sys.stdin.readline().strip()
	n = int (sys.stdin.readline().strip())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve (text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')