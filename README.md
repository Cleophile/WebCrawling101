# Python Web Crawling 101

## Legal Disclaimer

Codes in this section are only for academic uses, with no warranties or guarantees.  

## Requirements

For macOS: Python3.x, selenium chrome and chromedriver  

Make sure chromedriver is of the same version with chrome web browser

We recommand `homebrew` for downloading chromedriver. 

Simply runs:
`brew cask install chromedriver`

## Few Thoughts

This version of web crawling simply is a simulation of what people would do in the real world.
When you want to obtain some kind of information on the Internet, with only the help of your browser and your hands, what will you do?
Probably, you would search for results, copy some information, paste it somewhere else, then turn to the next page, copy some information, then paste it to somewhere else.
So, how can we make python, instead of ourselves, to finish the robotic, repeating work?

Selenium is a choice. Selenium can help us to operate web pages, to accomplish things like clicking the button, copy text from the page, adding text to the box, saving cookies, etc.  

Here we choose a simple case to find out how to analyze a webpage and how to use selenium to locate and apply operations to the elements on the webpage.

## Checklist

### 1. Locate the desired elements

