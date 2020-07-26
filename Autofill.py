from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver import Safari



#https://docs.google.com/forms/d/e/1FAIpQLSc5NC4HJX6hf8QqLhixRLwtGMisa4MYVmLV5ixPqYUIYJNHnw/viewform
def usingXpath():
    for person in driver.find_elements_by_class_name('freebirdFormviewerViewNumberedItemContainer'):
        question = person.find_element_by_xpath('.//div[@class="freebirdFormviewerComponentsQuestionBaseTitleDescContainer"]')

        print(" question  found",question.text)


        if (question.text.rstrip())=="10th Marks":
            print("answering",question.text )
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(tenthPercentage)
        # elif (question.text.rstrip())=="Address":
        #     ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
        #     ans.send_keys(address)
        elif (question.text.rstrip())=="Middle Name":
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(middleName)
        elif (question.text.rstrip())=="PUC percentage":
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(puPercentage)

        elif (question.text.rstrip())=="First Name":
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            
            ans.send_keys(firstName)

        elif (question.text.rstrip())=="Full Name":
            print("answering",question.text )
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(fullName)
        elif (question.text.rstrip())=="Last Name":
            print("answering",question.text )
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(lastName)

        elif (question.text.rstrip())=="Birthday date":
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys("17121999")

            continue
        elif (question.text.rstrip())=="Email ID":
            print("answering",question.text )
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(emailId)
        elif (question.text.rstrip())=="CGPA":
            print("answering",question.text )
            ans=person.find_element_by_xpath('.//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
            ans.send_keys(currentCgpa)
        else:
            print("answer not found for",  question.text)
            continue







driver = Safari()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc5NC4HJX6hf8QqLhixRLwtGMisa4MYVmLV5ixPqYUIYJNHnw/viewform?usp=sf_link")
driver.implicitly_wait(7000)




def checkform():
    try:
        assert "https://docs.google.com/forms/" in driver.current_url
        return True
    except:
        print("match not found")
        return False








fullName="Siddharth M Mallappa"
firstName="Siddharth"
middleName="M"
lastName="Mallappa"
emailId="siddharthm.cs17@bmsce.ac.in"
address="#390 Kaushik, 1st A Main Road, Girinager, Bangalore, 560085"
puPercentage="80.5"
puPCM="85"
tenthPercentage="8.4"
currentCgpa="8.33"
yearOfpassing="2021"
resumeLink="https://drive.google.com/drive/folders/1w4pqHIhhnpumMYZN_OPk4HGsOOG3nxuD?usp=sharing"

result=checkform()
if result:
    print(".. Valid ..")
    usingXpath()


else:
    print("Not google Form")

# /html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea

# attribute must be initialized
