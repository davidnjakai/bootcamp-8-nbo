class NotesApplication(object):
	def __init__(self,author,notes):
		self.author=author
		self.notes=notes
	def create(self, note_content):
		self.notes.append(note_content)
	def list(self):
		for i in self.notes:
			id=0
			print("Note ID: ",id)
			id+=1
			print("By Author ",self.author)
	def get(self, note_id):
		return self.notes[note_id]
	def search(self, search_text):
		pass
	def edit(self, note_id, new_content):
		self.notes[note_id]=new_content

