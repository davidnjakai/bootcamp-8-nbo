class NotesApplication(object):
	def __init__(self,author,notes):
		if type(notes) != type([]):
			self.notes = 'Invalid notes, it should be a list'
		else:
			self.notes=notes
		if type(author) != type(''):
			self.author = 'Invalid author name, it should be a string'
		else:
			self.author = author


	def create(self, note_content):
		if type(note_content) != type(''):
			return 'Invalid content, it should be a string'
		else:
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
		if type(search_text) != type(''):
			return 'search takes only a string as a parameter'
		id=0
		none_found = True
		res_dict = {}
		res_list = []
		res_dict['Header'] = "Showing results for search '{0}'".format(search_text)
		for i in self.notes:
			if search_text in i:
				none_found = False
				res_dict['Note ID'] = id
				res_dict['Content'] = i
				res_dict['Author'] = self.author
				res_list.append(res_dict)

			id+=1

		if none_found:
			return "Sorry, your search does not match any notes"
		else:
			return res_list


	def edit(self, note_id, new_content):
		if type(note_id) != type(1):
			return 'sorry, invalid ID given'
		if type(new_content) != type(''):
			return 'Invalid content, it should be a string'
		if note_id < len(self.notes) and note_id >= 0:
			self.notes[note_id]=new_content
		else:
			return "sorry, the note you're trying to edit does not exist"
