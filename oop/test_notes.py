import unittest
import notes

class NotesApplicationTest(unittest.TestCase):
	def test_return_empty_note_message():
		note = notes.NotesApplication('Tester', [])
		assertEqual(note.list(), "Sorry, there are no notes to display")

