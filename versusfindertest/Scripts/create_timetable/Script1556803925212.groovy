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

WebUI.click(findTestObject('Object Repository/Page_Home/a_Login'))

WebUI.setText(findTestObject('Page_Login/input_Username_username'), 'lulu')

WebUI.setEncryptedText(findTestObject('Page_Login/input_Password_password'), 'd/JjU8WmERS2ng5gWy3qxQ==')

WebUI.click(findTestObject('Page_Login/button_Login'))

WebUI.click(findTestObject('Object Repository/Page_Home/a_Dashboard'))

WebUI.click(findTestObject('Object Repository/Page_DashBoard/a_New availability'))

WebUI.click(findTestObject('Object Repository/Page_Timetable/input_Date end _btn btn-primary btn-lg'))

WebUI.click(findTestObject('Object Repository/Page_DashBoard/button_week'))

