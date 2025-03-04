import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
    
    def tearDown(self):
        """Clean up after tests"""
        pass
    
    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            self.assertIn("Show an instance based on class and ID", f.getvalue())
    
    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())
    
    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create NonExistentClass")
            self.assertIn("** class doesn't exist **", f.getvalue())
    
    def test_show_missing_id(self):
        """Test show command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertIn("** instance id missing **", f.getvalue())
    
    def test_show_invalid_id(self):
        """Test show command with invalid ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User 1234")
            self.assertIn("** no instance found **", f.getvalue())
    
    def test_destroy_missing_id(self):
        """Test destroy command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertIn("** instance id missing **", f.getvalue())
    
    def test_destroy_invalid_id(self):
        """Test destroy command with invalid ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User 1234")
            self.assertIn("** no instance found **", f.getvalue())
    
    def test_update_missing_id(self):
        """Test update command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertIn("** instance id missing **", f.getvalue())
    
    def test_update_invalid_id(self):
        """Test update command with invalid ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 1234 name John")
            self.assertIn("** no instance found **", f.getvalue())
    
    def test_count(self):
        """Test count command for a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertTrue(f.getvalue().strip().isdigit())
    
    def test_all(self):
        """Test all command without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue(isinstance(eval(f.getvalue().strip()), list))
    
    def test_all_with_class(self):
        """Test all command with class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertTrue(isinstance(eval(f.getvalue().strip()), list))
    
    def test_update_dict(self):
        """Test update with dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("1234", {"name": "John"})')
            self.assertIn("** no instance found **", f.getvalue())

if __name__ == "__main__":
    unittest.main()

