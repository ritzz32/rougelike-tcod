class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """
    def __init__(self, designation=None):

        designations = {
            'void': {'blocked': True, 'block_sight': True},
            'wall': {'blocked': True, 'block_sight': True},
            'floor': {'blocked': False, 'block_sight': False}
        }

        if designation is None:
            designation = 'void'

        metadata = designations.get(designation, {'blocked': True, 'block_sight': True})
        self.blocked = metadata.get('blocked')
        self.block_sight = metadata.get('block_sight')
