class TransactionPool:
    def __init__(self):
        self.transaction_map = {}


    def set_transaction(self, transaction):
        """
        Set a transaction in the transction pool.
        """
        self.transaction_map[transaction.id] = transaction