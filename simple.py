from faker import *
import random
import re

fake = Faker()
# Faker.seed(1337)

hbase_prefix = "put 'PEOPLE_DATA1', '"


class Person:

    def __init__(self):
        # Randomly decides gender
        self.gender = 'M' if random.randint(0, 1) == 0 else 'F'

        # creates profile based on gender
        # not all fields will be used

        self.data = fake.profile(sex=self.gender)
        profile = dict()

    def generatePerson(self):
        _data = self.data

        # bio fields

        _name = _data['name']
        _first_name = str(_name).split(" ")[0]
        _last_name = str(_name).split(" ")[1]
        _sex = _data['sex']
        _address = str(_data['address'])
        _blood_group = _data['blood_group']
        _residence = _data['residence']
        _homezip = str(_residence).split(" ")[-1]
        _homestate = str(_residence).split(" ")[-2]
        _company = _data['company']
        _birthdate = str(_data['birthdate'])
        _birthyear = str(_birthdate).split("-")[0]
        _birthmonth = str(_birthdate).split("-")[1]
        _birthday = str(_birthdate).split("-")[2]
        _job = _data['job']
        _ssn = _data['ssn']

        # Get rid of the Decimal part of return
        xlocation = str(_data['current_location'])
        __location = re.findall(r'\'(.*?)\'', xlocation)
        _tmp_location = __location[0] + ", " + __location[1]
        _current_location = _tmp_location

        _mail = _data['mail']

        # social fields
        _website = _data['website'][0]
        _username = _data['username']
        _friend1 = fake.name()
        _friend2 = fake.name()
        _friend3 = fake.name()
        linkedin = fake.url()
        facebook = fake.url()
        twitter = fake.url()
        hasLinkedin = 'Y' if random.randint(0, 1) == 0 else 'N'
        hasFacebook = 'Y' if random.randint(0, 1) == 0 else 'N'
        hasTwitter = 'Y' if random.randint(0, 1) == 0 else 'N'

        bio_fields = [_name, _first_name, _last_name, _sex, _blood_group, _residence, _company, _address, _homestate,
                      _homezip, _birthdate, _birthyear, _birthmonth, _birthday, _job, _ssn, _current_location, _mail]

        bio_field_list = ["_name", "_first_name", "_last_name", "_sex", "_blood_group", "_residence", "_company",
                          "_address", "_homestate",
                          "_homezip", "_birthdate", "_birthyear", "_birthmonth", "_birthday", "_job", "_ssn",
                          "_current_location", "_mail"]

        social_fields = [hasLinkedin, linkedin, hasFacebook, facebook, hasTwitter, twitter, _username, _friend1,
                         _friend2, _friend3, _website, _username]
        social_fields_list = ["hasLinkedin", "linkedin", "hasFacebook", "facebook", "hasTwitter", "twitter",
                              "_username", "_friend1", "_friend2", "_friend3", "_website", "_username"]

        for b in bio_fields:
            indexNum = bio_fields.index(b)
            indexVar = bio_field_list[indexNum]
            output = hbase_prefix + str(_ssn) + "', 'bio:" + str(indexVar) + "', '" + str(b) + "'" + "\n"

            f = open("output.txt", "a")
            f.write(output)
            f.close()

        for s in social_fields:
            indexNum = social_fields.index(s)
            indexVar = social_fields_list[indexNum]
            output = hbase_prefix + str(_ssn) + "', 'social:" + str(indexVar) + "', '" + str(s) + "'" + "\n"

            f = open("output.txt", "a")
            f.write(output)
            f.close()


for i in range(0, 200):
    i = Person()
    i.generatePerson()
