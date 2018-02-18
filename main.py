class ToDoList(object):
	def __init__(self):
		self.l=input('enter the list name:')
		self.t=[]
		self.d=[]

	def add(self):
		a=input('enter a new task:')
		self.t.append(a)
		print(self.t)

	def mark_done(self):
		b=input('enter the task which is done:')
		if b in self.t:
			self.d.append(b)
			self.t.remove(b)
		else:
			self.t.append(b)			

	def see_tasks(self):
		print(self.t)

	def done_tasks(self):
		print(self.d)		
