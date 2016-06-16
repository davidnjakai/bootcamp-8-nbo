class NotesApplication(object):
	def __init__(self,author,notes):
		self.author=author
		self.notes=notes


	def create(self, note_content):
		self.notes.append(note_content)


	def list(self):
		if self.notes != []:
			id=0
			for i in self.notes:
				print("Note ID: ",id)
				print(self.notes[id])
				id+=1
				print("By Author ",self.author)
		else:
			return "Sorry, there are no notes to display"


	def get(self, note_id):
		if note_id < len(self.notes) and note_id >= 0:
			return self.notes[note_id]
		else:
			return "Sorry, no such id"


	def search(self, search_text):
		id=0
		none_found = True
		print("Showing results for search'", search_text, "'")
		for i in self.notes:
			if search_text in i:
				none_found = False
				print("Note ID: ", id)
				print(i)
				print("By Author ", self.author)
			id+=1
		if none_found:
			print("Sorry, your search does not match any notes")


	def edit(self, note_id, new_content):
		if note_id < len(self.notes) and note_id >= 0:	
			self.notes[note_id]=new_content
		else:
			print("sorry, the note you're trying to edit does not exist")


