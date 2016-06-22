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

	def test_notes_attribute_is_list(self):
		note = notes.NotesApplication('Tester', 'invalid attribute')
		self.assertEqual(note.notes, 'Invalid notes, it should be a list')

	def test_author_attribute_is_string(self):
		note = notes.NotesApplication(['Tester'], [])
		self.assertEqual(note.author, 'Invalid author name, it should be a string')

	def test_creation_of_non_string_note(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(note.create(872), 'Invalid content, it should be a string')

	def test_none_string_in_search_method(self):
		note = notes.NotesApplication('Tester', [])
		self.assertEqual(note.search(23), 'search takes only a string as a parameter')

	def test_edit_with_non_string_content(self):
		note = notes.NotesApplication('Tester', ['my original note'])
		self.assertEqual(note.edit(0, 78), 'Invalid content, it should be a string')

	def test_edit_with_non_int_id_field(self):
		note = notes.NotesApplication('Tester', ['my original note'])
		self.assertEqual(note.edit('one', 'my edited note'), 'sorry, invalid ID given')

	def test_notes_attribute(self):
		note = notes.NotesApplication('Tester', ['my first note'])
		self.assertListEqual(note.notes, ['my first note'])

	def test_creation_of_extra_notes(self):
		note = notes.NotesApplication('Tester', ['my first note'])
		note.create('my second note')
		note.create('my third note')
		self.assertListEqual(note.notes, ['my first note', 'my second note', 'my third note'])

	def test_listing_of_notes_returns_None(self):
		note = notes.NotesApplication('Tester', ['my first note'])
		self.assertIsNone(note.list())

	def test_get_method_returns_required_note(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		self.assertEqual(note.get(1), 'my second note')

	def test_search_with_no_matching_result(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		self.assertEqual(note.search('dvorak'), 'Sorry, your search does not match any notes')

	def test_searching_with_one_matching_note(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		self.assertEqual(note.search('first'), [{'Header': "Showing results for search 'first'",\
		 'Note ID': 0, 'Content': 'my first note', 'Author': 'Tester'}])

	def test_searching_with_multiple_matching_notes(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		self.assertEqual(note.search('my'), [{'Author': 'Tester', 'Note ID': 2, 'Content': 'my third note', 'Header': "Showing results for search 'my'"},\
		 {'Author': 'Tester', 'Note ID': 2, 'Content': 'my third note', 'Header': "Showing results for search 'my'"},\
		 {'Author': 'Tester', 'Note ID': 2, 'Content': 'my third note', 'Header': "Showing results for search 'my'"}])

	def test_editing_of_non_existent_note(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		self.assertEqual(note.edit(3, 'my new content'), 'sorry, the note you\'re trying to edit does not exist')

	def test_editing_of_note_functions_as_required(self):
		note = notes.NotesApplication('Tester', ['my first note', 'my second note', 'my third note'])
		note.edit(1, 'edited second note')
		self.assertListEqual(note.notes, ['my first note', 'edited second note', 'my third note'])