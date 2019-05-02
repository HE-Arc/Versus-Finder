import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

WebUI.openBrowser('')

WebUI.navigateToUrl('https://vsfinder.srvz-webapp.he-arc.ch/home')

WebUI.click(findTestObject('Object Repository/profile/a_Login'))

WebUI.setText(findTestObject('Object Repository/profile/username'), 'lulu')

WebUI.setEncryptedText(findTestObject('Object Repository/profile/inputpwd'), 'd/JjU8WmERS2ng5gWy3qxQ==')

WebUI.click(findTestObject('Object Repository/profile/login'))

WebUI.click(findTestObject('Object Repository/profile/edit                              game profil'))

WebUI.selectOptionByValue(findTestObject('Object Repository/profile/select                                                                        BOWSER                                                                                BOWSER JR'), 
    '15', true)

WebUI.click(findTestObject('Object Repository/profile/skill'))

WebUI.click(findTestObject('Object Repository/profile/update'))

