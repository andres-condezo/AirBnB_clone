#!/usr/bin/python3
"""
This module containes test cases in the console
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Test cases class for Console"""

    def test_prompt(self):
        """ Test for the name in the prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_commnad_quit(self):
        """Test for command quit in the console"""
        self.assertTrue(HBNBCommand().onecmd('quit'))

    def test_command_EOF(self):
        """Test for command EOF in the console"""
        self.assertTrue(HBNBCommand().onecmd('EOF'))


class test_other_classes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_commnad_empty_line(self):
        """Test for the empty line"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual("", output.getvalue().strip())

    def test_command_classes(self):
        """Checks the classes in the console"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
            HBNBCommand().onecmd('.all()')
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())


class test_all_command(unittest.TestCase):
    """Test for all command in the console"""

    maxDiff = None

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_class_all_command(self):
        """Test for all command  in the console"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('all MyModel'))
            self.assertEqual(msg, output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('MyModel.all()'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_command_all_advanced(self):
        """Test for all command with advanced format"""

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())


class test_help_command(unittest.TestCase):
    """Test for help command in the console"""

    def test_help_EOF_command(self):
        """Test for help 'EOF' command in the console"""
        com_h = 'Quit command to exit the program'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help EOF'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_quit_command(self):
        """Test for help 'quit' command in the console"""
        com_h = 'Quit command to exit the program'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help quit'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_command_options(self):
        """Test for help command in the console"""
        com_h = ('Documented commands (type help <topic>):' +
                 '\n========================================' +
                 '\nEOF  all  count  create  destroy  help' +
                 '  quit  show  update')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_all_command(self):
        """Test for help 'all' command in the console"""
        com_h = 'Prints all string representation of all instances'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help all'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_count_command(self):
        """Test for help 'count' command in the console"""
        com_h = ('Retrieves the number of instances of a class' +
                 ': <class name>.count().')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help count'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_create_command(self):
        """Test for help 'create' command in the console"""
        com_h = ("Creates a new instance of BaseModel, " +
                 "saves it to a JSON file" +
                 "\n        and prints the 'id'")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help create'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_destroy_command(self):
        """Test for help 'destroy' command in the console"""
        com_h = 'Deletes an instance based on the class name and id'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help destroy'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_show_command(self):
        """Test for help 'show' command in the console"""
        com_h = ('Prints the string representation of an instance' +
                 '\n        based on the class name and id')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help show'))
            self.assertEqual(com_h, output.getvalue().strip())

    def test_help_update_command(self):
        """Test for help 'update' command in the console"""
        com_h = ('Updates an instance based on the class name' +
                 '\n        and id by adding or updating an attribute' +
                 '\n        Usage: update <class name> <id> <attribute name>' +
                 '\n        "<attribute value>"')
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('help update'))
            self.assertEqual(com_h, output.getvalue().strip())


class test_create_command(unittest.TestCase):
    """Test for create command in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_create_name_missing(self):
        """Test for create command with class name missing """
        msg = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_name_exist(self):
        """Test for create command with class invalid"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create MyModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_id(self):
        """test for create command with 'id' """
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id1 = output.getvalue().strip()
            self.assertFalse(HBNBCommand().onecmd('create BaseModel'))
            test_id2 = output.getvalue().strip()
            self.assertNotEqual(test_id1, test_id2)


class test_show_command(unittest.TestCase):
    """Test for show command in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_show_name_missing(self):
        """Test for show command with class name missing"""
        msg = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_name_exist(self):
        """Test for show command with class invalid"""
        msg = '** class doesn\'t exist **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show MyModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_id_missing(self):
        """Test for show command with id missing"""
        msg = '** instance id missing **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_id(self):
        """Test for show command with 'id' """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
            test_id = output.getvalue().strip()
            parameter_1 = 'show User {}'.format(test_id)
            parameter_2 = 'User.show("{}")'.format(test_id)
            comm_show1 = HBNBCommand().onecmd(parameter_1)
            comm_show2 = HBNBCommand().onecmd(parameter_2)
            self.assertEqual(comm_show1, comm_show2)

    def test_show_invalid_id(self):
        """Test for show command with invalid id """
        msg = '** no instance found **'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel 34'))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_more_than_one_arg(self):
        """Test for show command with invalid id """
        msg = '** no instance found **'
        parameter_1 = 'show BaseModel 34 other attr'
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(parameter_1))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_advanced_command(self):
        """Tests for show command with advanced format"""

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.show({})".format(test_id))
            com_1 = output.getvalue()
            self.assertIn(test_id, com_1)
            HBNBCommand().onecmd("all")
            com_2 = output.getvalue()
            self.assertIn(com_1, com_2)

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Place.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("City.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("State.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Review.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.show({})".format(test_id))
            self.assertIn(test_id, output.getvalue().strip())


class test_destroy_command(unittest.TestCase):
    """Test for destroy command in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_destroy_advanced_command(self):
        """Test for destroy command with advanced format"""

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.destroy({})".format(test_id))
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("User.destroy({})".format(test_id))
            HBNBCommand().onecmd("User.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Place.destroy({})".format(test_id))
            HBNBCommand().onecmd("Place.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("City.destroy({})".format(test_id))
            HBNBCommand().onecmd("City.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("State.destroy({})".format(test_id))
            HBNBCommand().onecmd("State.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Review.destroy({})".format(test_id))
            HBNBCommand().onecmd("Review.all()")
            self.assertNotIn(test_id, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.destroy({})".format(test_id))
            HBNBCommand().onecmd("Amenity.all()")
            self.assertNotIn(test_id, output.getvalue().strip())


class test_update_command(unittest.TestCase):
    """Test for update command in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_update_advanced_command(self):
        """Test for command update with advanced format"""

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_id = output.getvalue().strip()
            ptr = "update BaseModel {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "BaseModel.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Betty'))
            HBNBCommand().onecmd("BaseModel.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_id = output.getvalue().strip()
            ptr = "update User {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "User.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Tyrone'))
            HBNBCommand().onecmd("User.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_id = output.getvalue().strip()
            ptr = "update Place {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "Place.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Austin'))
            HBNBCommand().onecmd("Place.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_id = output.getvalue().strip()
            ptr = "update City {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "City.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Pablo'))
            HBNBCommand().onecmd("City.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_id = output.getvalue().strip()
            ptr = "update State {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "State.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Betty'))
            HBNBCommand().onecmd("State.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_id = output.getvalue().strip()
            ptr = "update Review {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "Review.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Pocoyo'))
            HBNBCommand().onecmd("Review.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_id = output.getvalue().strip()
            ptr = "update Amenity {} {} '{}'"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Jhon'))

        with patch("sys.stdout", new=StringIO()) as output:
            ptr = "Amenity.update({}, {}, '{}')"
            HBNBCommand().onecmd(ptr.format(test_id, 'first_name', 'Homero'))
            HBNBCommand().onecmd("Amenity.show({})".format(test_id))
            self.assertNotIn('Jhon', output.getvalue().strip())


class test_count_command(unittest.TestCase):
    """Test for count command in the console"""

    @classmethod
    def setUpClass(cls):
        if os.path.exists('file.json'):
            os.rename('file.json', 'temp')
        FileStorage._FileStorage__objects = dict()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('file.json'):
            os.remove('file.json')
        if os.path.exists('temp'):
            os.rename('temp', 'file.json')

    def test_command_classes(self):
        """Test for number of instances of a class"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create BaseModel')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create User')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('User.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create City')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('City.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create Place')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create State')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('State.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create Amenity')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create Review')

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Review.count()')
            obj_count = output.getvalue().strip()
            self.assertEqual('1', obj_count)
