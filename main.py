from Iterator import test as iterator_test
from Generator import test as generator_test


if __name__ == "--main__":
	try:
		iterator_test()
		generator_test()
	except Exception as error:
		print(error)
