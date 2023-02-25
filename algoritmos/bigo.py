# Se lee: f de n, o en función de n
# Donde n es el input
def f(n):
	# Loop que ejecutara n veces su contenido.
	for i in range(n): # 1 vez(for) por n (input)
		# Loop que ejecutara n veces su contenido durante n veces que se ejecute el loop superior.
		for j in range(n): # n veces(for) por n (input)
			print(i, j)
			

# print(2**1000000)
a, *b = 10, 20, 30

print(b)
print(type(b))