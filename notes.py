class NotesApplication(object):
	def __init__(self,author,notes):
		self.author=author
		self.notes=notes
	def create(self, note_content):
		self.notes.append(note_content)
	def list(self):
		if self.notes != [""]:
			for i in self.notes:
				id=0
				print("Note ID: ",id)
				id+=1
				print("By Author ",self.author)
		else:
			print("Sorry, there are no notes to display")
	def get(self, note_id):
		if note_id < len(self.notes) and note_id >= 0:
			return self.notes[note_id]
		else:
			print("Sorry, no such id")
	def search(self, search_text):
		pass
	def edit(self, note_id, new_content):
		if note_id < len(self.notes) and note_id >= 0:	
			self.notes[note_id]=new_content
		else:
			print("sorry, the note you're trying to edit does not exist")


