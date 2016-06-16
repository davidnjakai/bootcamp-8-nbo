import unittest
import notes

class NotesApplicationTest(unittest.TestCase):
	def test_return_empty_note_message(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(note.list(), "Sorry, there are no notes to display")

	def test_creating_a_note(self):
		note = notes.NotesApplication('Tester', [])
		note.create('sample note')
		self.assertEqual(note.notes[0], 'sample note')

	def test_instance_of_class_NotesApplication(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(type(note), type(notes.NotesApplication('Sample', [])))

	def test_get_non_existent_id(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(note.get(1), "Sorry, no such id")
					
	def test_search_function_in_empty_notes_list(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(note.search('searchstring'), "Sorry, your search does not match any notes")