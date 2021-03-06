from transaction import Transaction
from Crypto.Hash import SHA256
import time
import json

class Block:
	def __init__(self, index, transactions, previous_hash):
		# block initialization
		self.index = index
		self.timestamp = time.time()
		self.transactions = transactions
		self.nonce = 0
		self.previous_hash = previous_hash
		self.current_hash = self.calc_hash()

	def calc_hash(self):
		# calculates current hash of block
		block_string = json.dumps({
            "timestamp": self.timestamp,
            "transactions": [t.transaction_id for t in self.transactions],
			"nonce": self.nonce,
            "previous_hash": self.previous_hash
        }.__str__())
		return SHA256.new(block_string.encode("ISO-8859-2")).hexdigest()