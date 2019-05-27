from selenium import webdriver
import unittest
import time

class CasualViewerTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome('.\chromedriver.exe')

	def tearDown(self):
		self.browser.quit()
		
	def test_can_vote_on_curses_(self):
		#user visits the site, and sees the "cursed-economy" on the page:
		self.browser.get('http://localhost:8000')
		self.assertIn('Cursed Economy', self.browser.title)
		self.fail
		#user presented with two options
		
		#each curse option has a title and a short description
		
		#clicking puts focus on the selected option
		
		#a "submit" button appears"
		
		#user presses submit button
		
		#user is shown the vote count for those 2 items. 
		
		#user is presented with 2 new options
if __name__ == "__main__":
	unittest.main(warnings="ignore")