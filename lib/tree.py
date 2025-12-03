class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if not self.root:
      return None
    
    nodes_to_visit = [self.root]
    
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if node.get('id') == id:
        return node
      nodes_to_visit = node.get('children', []) + nodes_to_visit
    
    return None
