# python3
import sys

nodes = []

class Node(object):
  
    def __init__(self, label):
        self.label = label
        self.out = {}


def suffixTree(text):
    root = Node(None)
    root.out[text[0]] = Node(text)
    if not root.out[text[0]] in nodes:
        nodes.append(root.out[text[0]])

    for i in range(1, len(text)):
        curr_node = root
        j = i
        while j < len(text):
            if text[j] in curr_node.out:
                child = curr_node.out[text[j]]
                label = child.label
                k = j + 1
                while k-j < len(label) and text[k] == label[k-j]:
                    k += 1
                
                if k-j == len(label):
                    curr_node = child
                    j = k
                
                else:
                    cExist, cNew = label[k-j], text[k]
                    mid = Node(label[:k-j])
                    if not mid in nodes:
                        nodes.append(mid)
                        mid.out[cNew] = Node(text[k:])
                    if not mid.out[cNew] in nodes:
                        nodes.append(mid.out[cNew])
                    mid.out[cExist] = child
                    child.label = label[k-j:]
                    curr_node.out[text[j]] = mid
                    break
          
            else:
                curr_node.out[text[j]] = Node(text[j:])
                if not curr_node.out[text[j]] in nodes:
                    nodes.append(curr_node.out[text[j]])

  


def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  stree = suffixTree(text)

  for node in nodes:
      result.append(node.label)

  return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))