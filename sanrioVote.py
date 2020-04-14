from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json


class SanrioVote():
    def __init__(self, driver: webdriver.chrome.webdriver.WebDriver):
        self.driver = driver
        # Connect to selenium driver on container
        self.driver.get(CHARACTERS_URL)
        character_list = self.driver.find_element_by_class_name('characters_list').find_elements_by_tag_name('li')

        self.character_vote_dict = dict()  # {character_name: character_link_button}
        for c in character_list:
            character_name = c.find_element_by_class_name('charcterCard_nameText').text.replace(' ', '')
            link_button = c.find_element_by_class_name('charcterCard_button')
            self.character_vote_dict[character_name] = link_button

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        self.driver.close()

    def vote(self, character_name: str, age: int, gender: str, pref: str):
        # Enter to character page
        self.character_vote_dict[character_name].click()

        print("Voting", character_name)

        # answer survey
        forms = self.driver.find_elements_by_class_name('form_item')
        for i, form in enumerate(forms):
            value = [age, gender, pref][i]
            select = Select(form.find_element_by_class_name('selectBox_list'))
            select.select_by_visible_text(str(value))

        # Agree to terms of use
        term_checkbox = self.driver.find_element_by_id('terms')
        term_checkbox.click()

        # Vote
        vote_button = driver.find_element_by_class_name('form_voteButton')
        vote_button.click()  # Vote!


if __name__ == "__main__":
    # Set chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    CHARACTERS_URL = 'https://ranking.sanrio.co.jp/characters/'

    with open('vote.json', 'r') as f:
        j = json.load(f)

        CHARACTERS_NAME = j['characters']
        AGE = j['age']
        GENDER = j['gender']
        PREF = j['pref']
    print(CHARACTERS_NAME, AGE, GENDER, PREF)

    time.sleep(4)  # Waiting selenium boot

    for name in CHARACTERS_NAME:
        driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options,
        )
        with SanrioVote(driver) as sanrio_vote:
            sanrio_vote.vote(name, AGE, GENDER, PREF)
