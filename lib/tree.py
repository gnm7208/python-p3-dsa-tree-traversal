class Tree:
  """A tree data structure for DOM-like traversal."""
  
  def __init__(self, root=None):
    """Initialize tree with optional root node."""
    self.root = root

  def get_element_by_id(self, target_id):
    """Find and return the first node with the specified id."""
    # Return None if tree is empty
    if not self.root:
      return None
    
    # Initialize depth-first traversal queue
    nodes_to_visit = [self.root]
    
    while nodes_to_visit:
      # Process current node
      current_node = nodes_to_visit.pop(0)
      if current_node.get('id') == target_id:
        return current_node
      # Add children to front for depth-first traversal
      children = current_node.get('children', [])
      nodes_to_visit = children + nodes_to_visit
    
    return None
