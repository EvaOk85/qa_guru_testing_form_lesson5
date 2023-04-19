from selene import browser
from selene import have
import os



def test_form(size_browser_management):

    browser.open("/automation-practice-form")
    browser.element('#firstName').type('Mariya')
    browser.element('#lastName').type('Petrova')
    browser.element('#userEmail').type('PevRot@mail.ru')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type(7922691865)
    browser.element('.react-datepicker__input-container').click()
    browser.element('.react-datepicker__month-select ').click()
    browser.element('.react-datepicker__month-select  [value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select  [value="1985"]').click()
    browser.element('.react-datepicker__week [aria-label="Choose Monday, February 4th, 1985"]').click()
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys(os.getcwd()+'/tests.jpg')
    browser.element('#currentAddress').type('Voroshiliva')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').click()
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Mariya Petrova', 'Student Email PevRot@mail.ru', 'Gender Female', 'Mobile 7922691865',
        'Date of Birth 04 February,1985', 'Subjects English', 'Hobbies Sports',
        'Picture tests.jpg', 'Address Voroshiliva', 'State and City Haryana Panipat'))
