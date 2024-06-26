import unittest
from app import app, db, Todo

class TodoModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        # Clear the database
        Todo.query.delete()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_todo(self):
        todo = Todo(content='Test TODO')
        db.session.add(todo)
        db.session.commit()
        self.assertEqual(Todo.query.count(), 1)

    def test_delete_todo(self):
        todo = Todo(content='Test TODO')
        db.session.add(todo)
        db.session.commit()
        db.session.delete(todo)
        db.session.commit()
        self.assertEqual(Todo.query.count(), 0)

    def test_update_todo(self):
        todo = Todo(content='Test TODO')
        db.session.add(todo)
        db.session.commit()
        todo.content = 'Updated TODO'
        db.session.commit()
        updated_todo = Todo.query.get(todo.id)
        self.assertEqual(updated_todo.content, 'Updated TODO')

if __name__ == '__main__':
    unittest.main()
