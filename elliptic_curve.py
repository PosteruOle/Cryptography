class Point:
	def __init__(self):
		print('Point on a elliptic curve')
	
	def __str__(self):
		return f'Elliptic curve point!'

def main():
	p=Point()
	print(p)


if __name__=="__main__":
	main()					
