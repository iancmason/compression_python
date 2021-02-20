class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

def _compress(self, gene: str) -> None:
	self.bit_string: int = 1 #start with sentinel
	for nucleotide in gene.upper():
		self.bit_string <<=2 # shift left two bits
		if nucleotide == "A": # change last two bits to 00
		    self.bit_string |= 0b00
		if nucleotide == "C": #change last two bits to 01
		    self.bit_string |= 0b01
		if nucleotide == "G": #change last two bits to 10
		    self.bit_string |= 0b10 
		if nucleotide == "T": # change last two bits to 11
			self.bit_string |= 0b11
		else:
			raise ValueError("Invalid nucleotide: {}".format(nucleotide))

