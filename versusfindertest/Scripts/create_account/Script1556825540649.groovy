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

WebUI.click(findTestObject('Object Repository/Page_Home/a_Sign up'))

WebUI.setText(findTestObject('Object Repository/Page_Sign Up/input_Username_username'), 'test3')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Sign Up/input_Password_password1'), '8SQVv/p9jVTmGBHPxE6phQ==')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Sign Up/input_Confirm password_password2'), '8SQVv/p9jVTmGBHPxE6phQ==')

WebUI.sendKeys(findTestObject('Object Repository/Page_Sign Up/input_Confirm password_password2'), Keys.chord(Keys.ENTER))

WebUI.setText(findTestObject('Page_Login/input_Username_username (5)'), 'test3')

WebUI.setEncryptedText(findTestObject('Page_Login/input_Password_password (5)'), '8SQVv/p9jVTmGBHPxE6phQ==')

WebUI.sendKeys(findTestObject('Page_Login/input_Password_password (5)'), Keys.chord(Keys.ENTER))

