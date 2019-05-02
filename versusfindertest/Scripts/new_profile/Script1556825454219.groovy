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

WebUI.click(findTestObject('Object Repository/Page_Home/a_Login (4)'))

WebUI.setText(findTestObject('Page_Login/input_Username_username (4)'), 'test')

WebUI.setEncryptedText(findTestObject('Page_Login/input_Password_password (4)'), '8SQVv/p9jVTmGBHPxE6phQ==')

WebUI.sendKeys(findTestObject('Page_Login/input_Password_password (4)'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('Object Repository/Page_Home/a_New                                            game profil'))

WebUI.setText(findTestObject('Object Repository/Page_New profile for Super Smash Bros Ultimate/input_Pseudo_input_pseudo'), 
    'testminator')

WebUI.setText(findTestObject('Object Repository/Page_New profile for Super Smash Bros Ultimate/input_Battletag_input_battletag'), 
    '12-1222-1222-1222')

WebUI.click(findTestObject('Object Repository/Page_New profile for Super Smash Bros Ultimate/button_New profil'))

