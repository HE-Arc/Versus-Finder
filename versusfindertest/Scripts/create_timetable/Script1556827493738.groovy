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

WebUI.click(findTestObject('Object Repository/a_Login'))

WebUI.setText(findTestObject('Page_Login/input_Username_username'), 'test')

WebUI.setEncryptedText(findTestObject('Page_Login/input_Password_password'), '8SQVv/p9jVTmGBHPxE6phQ==')

WebUI.click(findTestObject('Page_Login/button_Login'))

WebUI.click(findTestObject('Object Repository/a_SSBU (1)'))

WebUI.click(findTestObject('Object Repository/a_Game informations (1)'))

WebUI.click(findTestObject('Object Repository/a_Search an opponent'))

WebUI.click(findTestObject('Object Repository/button_Search'))

WebUI.click(findTestObject('Object Repository/input_Jan 1 2020 noon_btn btn-primary'))

WebUI.click(findTestObject('Object Repository/a_SSBU (1)'))

WebUI.click(findTestObject('Object Repository/a_Game informations (1)'))

WebUI.click(findTestObject('Object Repository/button_The matchs to come_fc-prev-button fc-button fc-state-default fc-corner-left fc-state-hover'))

WebUI.click(findTestObject('Object Repository/button_The matchs to come_fc-prev-button fc-button fc-state-default fc-corner-left fc-state-hover'))

