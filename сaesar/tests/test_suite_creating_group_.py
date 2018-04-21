from resource.constants_creating_group import TEST_TOO_LONG_GROUP_NAME, \
    MESSAGE_NAME_IS_MORE_20_CHAR, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME, \
    MESSAGE_DIRECTION_IS_NOT_SELECTED, \
    MESSAGE_START_DATE_FIELD_IS_EMPTY, APP_TITLE, TEST_GROUP_NAME, \
    TEST_ITERATIONS, MESSAGE_EMPTY_EXPERT_NAME, TEST_SECOND_EXPERT_NAME, \
    MESSAGE_INVALID_EXPERT_NAME, TEST_THIRD_EXPERT_NAME, TEST_LOCATION, TEST_DIRECTION, TEST_TEACHERS_NAME, \
    TEST_START_DATE, TEST_FINISH_DATE, TEST_WRONG_FORMAT_DATE, MESSAGE_WRONG_START_DATE, \
    MESSAGE_FINISH_DATE_FIELD_IS_EMPTY, TEST_FIRST_EXPERT_NAME
from resource.users_base import first_admin
from tests.test_base import TestBase
from resource.error_handler import logger_exception


class TestCreatingGroup(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.left_menu = self.group_page.open_left_menu()
        self.left_menu.create_group_button().click()

    @logger_exception
    def test01_name_entering_is_enabled(self):
        """ Check  the field 'name'  is enabled"""
        field_name_of_group = self.group_page.CreateGroupWindow(). \
            get_group_name_field()
        self.assertTrue(field_name_of_group.is_enabled())

    @logger_exception
    def test02_select_direction_is_enabled(self):
        """ Check  the field 'direction'  is enabled"""
        field_direction = self.group_page.CreateGroupWindow(). \
            get_group_direction()
        self.assertTrue(field_direction.is_enabled())

    @logger_exception
    def test03_select_location_is_enabled(self):
        """ Check  the field 'location'  is enabled"""
        field_location = self.group_page.CreateGroupWindow(). \
            get_group_location()
        self.assertTrue(field_location.is_enabled())

    @logger_exception
    def test04_adding_more_5_teachers(self):
        """ Check  adding more 5 teachers, while there is only 5 teachers
        are presented in drop list"""
        i = TEST_ITERATIONS
        while i > 0:
            self.group_page.CreateGroupWindow().add_teacher()
            i -= 1
        teachers_list = self.group_page.CreateGroupWindow(). \
            get_values_from_added_teachers_list()
        self.assertEqual(teachers_list.sort(), list(set(teachers_list)).sort())

    @logger_exception
    def test05_save_button_is_enabled(self):
        """ Check  the field 'save' button  is enabled"""
        save_button = self.group_page.CreateGroupWindow(). \
            get_save_group_button()
        self.assertTrue(save_button.is_enabled)

    @logger_exception
    def test06_save_button_is_working(self):
        """ Check  the field 'save' button  work correct """
        self.group_page.CreateGroupWindow().auto_fill_all_fields(
            TEST_GROUP_NAME, TEST_LOCATION, TEST_DIRECTION, TEST_TEACHERS_NAME,
            TEST_FIRST_EXPERT_NAME, TEST_START_DATE)
        self.assertEqual(self.group_page.get_title_name(), APP_TITLE)

    @logger_exception
    def test07_cancel_button_is_enabled(self):
        """ Check  the field 'cancel' button  is enabled"""
        cancel_button = self.group_page.CreateGroupWindow(). \
            cancel_button_get()
        self.assertTrue(cancel_button.is_enabled())

    @logger_exception
    def test08_cancel_button_is_working(self):
        """ Check  the field 'save' button  work correct """
        cancel_button = self.group_page.CreateGroupWindow(). \
            cancel_button_get()
        cancel_button.click()
        self.assertEqual(self.group_page.get_title_name(), APP_TITLE)

    @logger_exception
    def test09_create_group_with_more_20_char_name(self):
        """ Check  the creating of group when the length of name is more than 20 characters"""
        self.group_page.CreateGroupWindow().set_group_name(
            TEST_TOO_LONG_GROUP_NAME)
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name = self.group_page.CreateGroupWindow(). \
            get_group_name_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(form_group_name)
        self.assertEqual(warning_message, MESSAGE_NAME_IS_MORE_20_CHAR)

    @logger_exception
    def test10_create_group_with_empty_field_group_name(self):
        """ Check  the creating of group when the  field 'name' is empty"""
        self.group_page.CreateGroupWindow().set_group_name('')
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name = self.group_page.CreateGroupWindow(). \
            get_group_name_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(form_group_name)
        self.assertEqual(warning_message, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME)

    @logger_exception
    def test11_create_group_with_empty_field_direction(self):
        """ Check  the creating of group when the  field 'direction' is empty"""
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        direction_form = self.group_page.CreateGroupWindow(). \
            get_group_direction_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(direction_form)
        self.assertEqual(warning_message, MESSAGE_DIRECTION_IS_NOT_SELECTED)

    @logger_exception
    def test12_create_group_with_empty_start_date(self):
        """ Check  the creating of group when the  field 'start date' is empty"""
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        start_date_form = self.group_page.CreateGroupWindow(). \
            get_start_date_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(start_date_form)
        self.assertEqual(warning_message, MESSAGE_START_DATE_FIELD_IS_EMPTY)

    @logger_exception
    def test13_add_expert_without_name(self):
        """ Check  the adding of expert with empty field 'name'"""
        self.group_page.CreateGroupWindow().add_expert_x('')
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertEqual(warning_message, MESSAGE_EMPTY_EXPERT_NAME)

    @logger_exception
    def test14_add_expert_non_valid_name(self):
        """ Check  the adding of expert with number in field 'name'"""
        self.group_page.CreateGroupWindow().add_expert(TEST_SECOND_EXPERT_NAME)
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertEqual(warning_message, MESSAGE_INVALID_EXPERT_NAME)

    @logger_exception
    def test15_adding_more_5_same_expert(self):
        """ Check  the adding of 20 experts with same value in field 'name'"""
        for i in range(0, TEST_ITERATIONS):
            self.group_page.CreateGroupWindow().add_expert(
                TEST_THIRD_EXPERT_NAME)
        experts_list = self.group_page.CreateGroupWindow(). \
            get_added_experts_list()
        self.assertEqual(experts_list, list(set(experts_list)))

    @logger_exception
    def test16_add_expert_empty_name(self):
        """ Check  the adding of expert with empty field 'name'"""
        self.group_page.CreateGroupWindow().add_expert(
            TEST_THIRD_EXPERT_NAME)
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertEqual(warning_message, MESSAGE_INVALID_EXPERT_NAME)

    @logger_exception
    def test17_add_empty_teacher(self):
        """ Check  adding  teacher, with empty name"""
        for i in range(0, TEST_ITERATIONS):
            self.group_page.CreateGroupWindow().add_teacher()
        teachers_list = self.group_page.CreateGroupWindow(). \
            get_values_from_added_teachers_list()
        self.assertNotIn('', teachers_list)

    @logger_exception
    def test18_add_default_teacher(self):
        """ Check  adding  teacher, without choosing him from list"""
        self.group_page.CreateGroupWindow().add_teacher()
        teachers_list = self.group_page.CreateGroupWindow(). \
            get_values_from_added_teachers_list()
        self.assertIn(TEST_TEACHERS_NAME, teachers_list)

    @logger_exception
    def test19_check_autoincrement_finish_date(self):
        """ Check  the autoincrement of ''finish date' field  after entering 'start date' field"""
        self.group_page.CreateGroupWindow().set_start_date(TEST_START_DATE)
        finish_date_value = self.group_page.CreateGroupWindow().get_value_finish_date_field()
        self.assertEqual(finish_date_value, TEST_FINISH_DATE)

    @logger_exception
    def test20_check_autoincrement_finish_date(self):
        """ Check  the autoincrement of ''start date' field  after entering ' finish date' field"""
        self.group_page.CreateGroupWindow().set_finish_date(TEST_FINISH_DATE)
        start_date_value = self.group_page.CreateGroupWindow().get_value_start_date_field()
        self.assertEqual(start_date_value, TEST_START_DATE)

    @logger_exception
    def test21_create_group_with_wrong_format_start_date(self):
        """ Check  the creating of group when the  field 'start date' get wrong date format"""
        self.group_page.CreateGroupWindow().set_start_date(TEST_WRONG_FORMAT_DATE)
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        start_date_form = self.group_page.CreateGroupWindow(). \
            get_start_date_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(start_date_form)
        self.assertEqual(warning_message, MESSAGE_WRONG_START_DATE)

    @logger_exception
    def test22_create_group_with_wrong_format_finish_date(self):
        """ Check  the creating of group when the  field 'finish date' get wrong date format"""
        self.group_page.CreateGroupWindow().set_finish_date(TEST_WRONG_FORMAT_DATE)
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        finish_date_form = self.group_page.CreateGroupWindow(). \
            get_finish_date_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(finish_date_form)
        self.assertEqual(warning_message, MESSAGE_WRONG_START_DATE)

    @logger_exception
    def test23_create_group_with_empty_finish_date(self):
        """ Check  the creating of group when the  field 'finish date' is empty"""
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        finish_date_form = self.group_page.CreateGroupWindow(). \
            get_finish_date_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(finish_date_form)
        self.assertEqual(warning_message, MESSAGE_FINISH_DATE_FIELD_IS_EMPTY)

    @logger_exception
    def test24_add_teacher_by_name(self):
        """ Check  adding  teacher, with custom selected name"""
        self.group_page.CreateGroupWindow().select_teacher(TEST_TEACHERS_NAME)
        teachers_list = self.group_page.CreateGroupWindow(). \
            get_values_from_added_teachers_list()
        self.assertIn(TEST_TEACHERS_NAME, teachers_list)