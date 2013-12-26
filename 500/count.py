import collections

class GeometricProgressions:
	def count(self, b1, q1, n1, b2, q2, n2):
    s = set()
    self._add_set(b1, q1, n1, s)
		self._add_set(b2, q2, n2, s)



	def _add_set(self, b, q, n, s):
		b_primes = Counter()
		q_primes = Counter()
		if b == 0 or q == 0:
			b_primes[0] = 0
			s.add(b_primes)
			return

		self._prime_decomposition(b, b_primes)
		self._prime_decomposition(q, q_primes)
		for _ in xrange(n):
			s.add(b_primes)
			for k, v in q_primes.items():
				b_primes[k] += v 

	def _prime_decomposition(self, n, d):
		for i in xrange(2, 22361):
			while n % i == 0:
				d[i] 

