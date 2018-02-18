from main import ToDoList

todo=ToDoList()
while True:
	choice=int(input('what would you like to do?\n \
		1.Add todo tasks\n \
		2.Add tasks to done\n \
		3.See tasks\n \
		4.Exit\n'))
	if choice==1:
		todo.add()
	elif choice==2:
		todo.mark_done()
	elif choice==3:
		f=int(input('\n1.See todo list\n2.See done tasks\n'))
		if f==1:
			todo.see_tasks()
		else:
			todo.done_tasks()
	else:
		break			
			
			















			

