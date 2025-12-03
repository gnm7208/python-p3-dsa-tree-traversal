class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, target_id):
    # Return None if tree is empty
    if not self.root:
      return None
    
    # Initialize depth-first traversal
    nodes_to_visit = [self.root]
    
    while nodes_to_visit:
      # Process current node
      node = nodes_to_visit.pop(0)
      if node.get('id') == target_id:
        return node
      # Add children to front for depth-first
      nodes_to_visit = node.get('children', []) + nodes_to_visit
    
    return None
