class Block:
    """
    Block: a unit of storage.
    Store transactons in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f'Block: {self.data}'