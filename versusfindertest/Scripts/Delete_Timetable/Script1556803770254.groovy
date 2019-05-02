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

WebUI.click(findTestObject('Page_Home/a_Login (3)'))

WebUI.setText(findTestObject('Object Repository/Page_Login/input_Username_username (3)'), 'lulu')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Login/input_Password_password (3)'), 'd/JjU8WmERS2ng5gWy3qxQ==')

WebUI.sendKeys(findTestObject('Object Repository/Page_Login/input_Password_password (3)'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('Page_Home/a_Dashboard (1)'))

WebUI.click(findTestObject('Object Repository/Page_DashBoard/div_3p SmashBros'))

WebUI.click(findTestObject('Object Repository/Page_DashBoard/button_OK'))

