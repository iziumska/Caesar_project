from selenium.webdriver.common.by import By


class LogInLocators(object):
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    CONFIRM_ACTION = (By.CLASS_NAME, 'submit')
    FIELD_MESSAGE = (By.CLASS_NAME, 'message')


class GroupPageLocators(object):
    GROUP_LOCATION = (By.CLASS_NAME, 'groupLocation')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'div.search')

    BUTTON_MY_GROUPS = (By.CLASS_NAME, 'myGroups')
    BUTTON_ALL_GROUPS = (By.CLASS_NAME, 'allGroups')
    BUTTONS_STAGE_GROUPS = (By.CLASS_NAME, 'stage-toggle')

    ENDED_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(2)')
    CURRENT_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(4)')
    BOARDING_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(6)')

    GROUPS = (By.CLASS_NAME, 'small-group-view')

    # main section
    GROUP_NAME = (By.CLASS_NAME, 'content-header-group-name')
    BUTTON_EDIT_GROUP = (By.NAME, 'edit')
    BUTTON_INFO_GROUP = (By.NAME, 'info')
    BUTTON_STUDENTS_IN_GROUP = (By.NAME, 'students')
    BUTTON_SCHEDULE_GROUP = (By.NAME, 'shedule')
    BUTTON_MESSAGE_GROUP = (By.NAME, 'message')

    GROUP_COORDINATION = (By.CLASS_NAME, 'group_coordination')
    GROUP_INFO = (By.CLASS_NAME, 'group_info')
    KEY_DATES = (By.CLASS_NAME, 'key - dates')
    GROUP_STAGE_TITLE = (By.CLASS_NAME, 'groupStageTitle')
    GROUP_STAGE = (By.CLASS_NAME, 'groupStage')

    LEFT_MENU = (By.CSS_SELECTOR, '#left-menu > div')
    USER_PHOTO = (By.CLASS_NAME, 'user-photo')
    TOP_MENU = (By.CLASS_NAME, 'row')
    BUTTON_CONFIRM_DELETION = \
        (By.CSS_SELECTOR, '#modal-window > div > div >'
                          ' div > div > button.btn.btn-delete > i')
    BUTTON_CANCEL_DELETION = \
        (By.CSS_SELECTOR, '#modal-window > div > div >'
                          ' div > div > button.btn.btn-cancel > i')


class RightMenuLocators(object):
    BUTTON_EDIT_PROFILE = (By.CLASS_NAME, 'btn-edit')
    USER_NAME = (By.CLASS_NAME, 'name')
    USER_ROLE = (By.CLASS_NAME, 'role')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, 'a.logout:nth-child(3)')


class LeftMenuLocators(object):
    BUTTON_CREATE_GROUP = (By.XPATH, '//*[@title = "Create"]')
    BUTTON_SEARCH_GROUP = (By.XPATH, '//*[@title = "Search"]')
    BUTTON_EDIT_GROUP = (By.XPATH, '//*[@title = "Edit"]')
    BUTTON_DELETE_GROUP = (By.XPATH, '//*[@title = "Delete"]')


class TopMenuLocators(object):
    LOCATIONS_BUTTON = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(1)')
    GROUPS_BUTTON_ = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(2)')
    STUDENTS_BUTTON = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(3)')
    SCHEDULE_BUTTON = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(4)')
    ADD_BUTTON = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(5)')
    ABOUT_BUTTON = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(6)')

    BUTTON_LOGOUT = (By.CLASS_NAME, 'logout')


class LocationWindowLocators(object):
    CHERNIVTSY_LOCATION =\
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[1]/p')
    DNIPRO_LOCATION =\
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[2]/p')
    IVANO_FRANKIVSK_LOCATION =\
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[3]/p')
    KYIV_LOCATION =\
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[4]/p')
    LVIV_LOCATION = \
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[5]/p')
    RIVNE_LOCATION = \
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[6]/p')
    SOFIA_LOCATION =\
        (By.XPATH, '//*[@id="modal-window"]/div/div/div/ul/li[7]/p')
    SAVE_BUTTON = \
        (By.CSS_SELECTOR, '#modal-window > div > div '
                          '> div > div > button.save > i')
    DISABLED_SAVE_BUTTON = \
        (By.CSS_SELECTOR, '#modal-window > div '
                          '> div > div > div > button.save.disabled')
    CANCEL_BUTTON = \
        (By.CSS_SELECTOR, '#modal-window > div > div '
                          '> div > div > button.cancel > i')


class AdminPageLocators(object):
    ADD_USER = (By.XPATH, ".//*[text()='Add user']")
    ADD_GROUP = (By.XPATH, "/.//*[text()='Add group']")
    ADD_STUDENT = (By.XPATH, ".//*[text()='Add student']")
    TAB_USERS = (By.CSS_SELECTOR, "a[href*='users']")
    TAB_GROUPS = (By.CSS_SELECTOR, "a[href*='groups']")
    TAB_STUDENTS = (By.CSS_SELECTOR, "a[href*='students']")
    BUTTON_ESCAPE = (By.CSS_SELECTOR, '.btn.btn-warning.home')
    TITLE_ENTITY = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.submit")

    @staticmethod
    def get_request_table(table):
        table = ".//*[@id='{type}']/div/table/tbody//td[position()<last()]" \
            .format(type=table)
        return table


class CreateEditUsersLocators(object):
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    ROLE = (By.NAME, "role")
    LOCATION = (By.NAME, "location")
    PHOTO = (By.NAME, "photo")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    DELETE_BUTTONS = "(//tbody//button[@class='btn btn-danger delete'])"


class CreateEditGroupsLocators(object):
    NAME = (By.NAME, "name")
    LOCATION = (By.NAME, "location")
    DIRECTION = (By.NAME, "direction")
    START_DATE = (By.NAME, "startDate")
    FINISH_DATE = (By.NAME, "finishDate")
    TEACHERS = (By.NAME, "teachers")
    EXPERTS = (By.NAME, "experts")
    STAGE = (By.NAME, "stage")
    BUDGET = (By.NAME, "budgetOwner")


class CreateGroupWindowLocators(object):
    GROUP_NAME_FORM = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(1) > div:nth-child(1) > div > div')
    GROUP_NAME_FIELD = (By.NAME, 'name')
    DIRECTION_FORM = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(3) > div:nth-child(1)')
    DIRECTION_DROP_LIST = (By.NAME, 'direction')
    LOCATION_DROP_LIST = (By.NAME, 'location')
    ONE_MORE_TEACHER_BUTTON = (By.CLASS_NAME, 'add-teacher-btn')
    TEACHERS_DROP_LIST = (By.NAME, 'teacher')
    ACCEPT_TEACHER_BUTTON = (By.ID, 'acceptSelect')
    ADDED_TEACHERS_FORM = (By.CLASS_NAME, 'list-item')
    BUDGET_SOFT_SERVE_BUTTON = (By.CLASS_NAME,
                                'btn btn-default budget-option active')
    BUDGET_OPEN_GROUP_BUTTON = \
        (By.CLASS_NAME, 'btn btn-default budget-option ')
    START_DATE_FORM = (
        By.CSS_SELECTOR, '#modal-window > section > section > section > '
                         'div:nth-child(3) > '
                         'div.form-group.col-xs-6.col-xs-offset-0.col-md-5.'
                         'col-md-offset-1.col-lg-4.calendar-wrapper')
    START_DATE_FIELD = (By.NAME, 'startDate')
    FINISH_DATE_FIELD = (By.NAME, 'finishDate')
    ADD_EXPERT_BUTTON = (By.CLASS_NAME, 'add-expert-btn')
    EXPERTS_NAME_FIELD = (By.NAME, 'expert')
    ACCEPT_EXPERT_BUTTON = (By.ID, 'acceptInput')
    SAVE_BUTTON = (By.ID, 'save')
    CANCEL_BUTTON = (By.ID, 'cancel')


class CreateEditStudentsLocators(object):
    GROUP_ID = (By.NAME, 'groupID')
    NAME = (By.NAME, "name")
    LAST_NAME = (By.NAME, "lastName")
    ENGLISH_LEVEL = (By.NAME, "englishLevel")
    CV_URL = (By.NAME, "CvUrl")
    IMAGE = (By.NAME, "imageUrl")
    ENTRY_SCORE = (By.NAME, "entryScore")
    APPROVED_BY = (By.NAME, 'approvedBy')


class StudentsListLocators(object):
    EDIT_STUDENTS_LIST_BUTTON = \
        (By.XPATH, './/*[@id="main-section"]/div/header/div[1]/button')
    GROUP_INFO_BUTTON = (By.CSS_SELECTOR, '.btn.infoBtn.active')
    STUDENTS_IN_STUDENTS_LIST_BUTTON = \
        (By.XPATH, './/*[@id="main-section"]/div/header/div[2]/button[2]')
    SCHEDULE_IN_STUDENTS_BUTTON = (By.CLASS_NAME, 'shedule')
    MESSAGE_IN_STUDENTS_BUTTON = (By.CLASS_NAME, 'message')
    STUDENTS_LISTS_ROWS = (By.CLASS_NAME, 'tableBodyStudents')
    SORT_LIST_BY_NAME_BUTTON = (By.CLASS_NAME, 'fullName')
    SORT_LIST_BY_ENGLISH_LEVEL_BUTTON = (By.CLASS_NAME, 'engLevel')
    NAME_STUDENT_LIST = \
        (By.CSS_SELECTOR, '.header-modal-editStudentlist > span:nth-child(1)')
    STUDENTS_TABLE = (By.CLASS_NAME, 'tableBodyStudents')
    EXIT_EDIT_STUDENTS_LIST_BUTTON = (By.CLASS_NAME, 'exit')
    DELETE_STUDENT_BUTTON = (By.XPATH, './/*[@id="modal-window"]//td[6]/i')
    CONFIRM_DELETING_BUTTON = (By.XPATH, './/*[@id="modal-window"]//button[1]')
    ADD_NEW_STUDENT_BUTTON = \
        (By.XPATH, './/*[@id="modal-window"]/section//button[1]')
    EDIT_STUDENT_BUTTON = \
        (By.XPATH, './/*[@id="modal-window"]/section//td[5]/i')


class StudentLocators(object):
    FIRST_NAME_TEXT_FIELD = \
        (By.XPATH, './/*[@id="modal-window"]//div[2]/div[1]/input')
    LAST_NAME_TEXT_FIELD = \
        (By.XPATH, './/*[@id="modal-window"]//div[3]/div[1]/input')
    LIST_ENGLISH_LEVEL = \
        (By.XPATH, './/*[@id="modal-window"]//div[4]/div[1]/select')
    PRE_INTERMEDIATE_LOW = \
        (By.XPATH, './/*[@id = "modal-window"]//div[4]/div[1]/'
                   'select/option[2]')
    STUDENT_MARK_INCOMING_TEST = \
        (By.XPATH, './/*[@id="modal-window"]//div[1]/div[2]/input')
    STUDENT_ENTRY_SCORE = \
        (By.XPATH, './/*[@id="modal-window"]//div[2]/div[2]/input')
    STUDENT_APPROVED_BY = \
        (By.XPATH, './/*[@id="modal-window"]//div[3]/div[2]/select')
    APPROVED_BY = \
        (By.XPATH, './/*[@id="modal-window"]//div[3]/div[2]/select/option[2]')
    SAVE_CHANGES_BUTTON = \
        (By.XPATH, './/*[@id="modal-window"]//div[6]/button[1]')
    ADD_CV_BUTTON = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[1]/button')
    INPUT_PATH_CV_FILE = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[1]/input')
    FILE_CV = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[1]/ul/li')
    FILE_NAME_CV = (By.CSS_SELECTOR, 'span')
    ADD_PHOTO_BUTTON = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[2]/button')
    INPUT_PATH_PHOTO_FILE = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[2]/input')
    FILE_NAME_PHOTO = \
        (By.XPATH, './/*[@id="modal-window"]//div[5]/div[2]/ul/li/span[1]')
    WARNINGS_ADD_EMPTY_STUDENT_DATA = (By.CLASS_NAME, 'hint')
