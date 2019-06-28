import tcod as libtcod

class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """
    def __init__(self, colors, designation=None):
        self.blocked = None
        self.block_sight = None
        self.colors = colors
        self.color = None

        if designation is None:
            designation = 'void'
        self.designate(designation)

    def designate(self, designation):

        designations = {
            'void': {'blocked': True, 'block_sight': True},
            'dark_wall': {'blocked': True, 'block_sight': True},
            'dark_ground': {'blocked': False, 'block_sight': False}
        }

        metadata = designations.get(designation, {'blocked': True, 'block_sight': True})
        self.blocked = metadata.get('blocked')
        self.block_sight = metadata.get('block_sight')

        if designation in self.colors:
            self.color = self.colors[designation]
        else:
            self.color = libtcod.purple
