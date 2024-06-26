import unittest
from app import app, db, Todo

class TodoRoutesTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_todo(self):
        with app.app_context():
            response = self.app.post('/add', data={'content': 'Test Todo'})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Todo.query.count(), 1)

    def test_delete_todo(self):
        with app.app_context():
            todo = Todo(content="Test Todo")
            db.session.add(todo)
            db.session.commit()
            response = self.app.get(f'/delete/{todo.id}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Todo.query.count(), 0)

if __name__ == '__main__':
    unittest.main()
