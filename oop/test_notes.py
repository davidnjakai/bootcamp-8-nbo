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