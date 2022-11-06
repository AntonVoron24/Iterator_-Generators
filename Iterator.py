class FlatIterator:

	def __init__(self, list_of_list):
		self.list_of_list = list_of_list

	def __iter__(self):
		self.queue = []  # определяем вложенный список для добавления элементов очереди
		self.cursor = iter(self.list_of_list)  # определяем итератор для списка списков
		return self

	def __next__(self):
		"""Определяет и возвращает следущий элемент списка списков"""
		while True:
			try:
				self.element = next(self.cursor)  # получаем следующий элемент списка
			except StopIteration:  # если следующего элемента нет получаем исключение
				if not self.queue:  # если не осталось элементов в очереди, возвращаем исключение
					raise StopIteration
				else:
					self.cursor = self.queue.pop()  # или получаем следующий элемент очереди
					continue
			if isinstance(self.element, list):  # проверяем тип элемента на принадлежность к списку
				self.queue.append(self.cursor)  # если список, то добавляем в очередь
				self.cursor = iter(self.element)  # и смещаем указатель текущего итератора
			else:  # если элемент не список, то возвращаем этот элемент
				return self.element


def test():
	list_of_lists_2 = [
		[['a'], ['b', 'c']],
		['d', 'e', [['f'], 'h'], False],
		[1, 2, None, [[[[['!']]]]], []]
	]

	for flat_iterator_item, check_item in zip(
			FlatIterator(list_of_lists_2),
			['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
	):
		assert flat_iterator_item == check_item

	assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
	test()
