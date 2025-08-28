class WebBrowser:
    connected = True

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False


chrome = WebBrowser('Facebook.com')
firefox = WebBrowser('Google.com')
print(chrome.__dict__)  # class variable is not present
print(firefox.__dict__)  # class variable is not present

print(chrome.connected)
print(firefox.connected)

chrome.connected = False

print(chrome.__dict__)  # class variable is not present
print(firefox.__dict__)  # class variable is not present

print(chrome.connected)
print(firefox.connected)

WebBrowser.connected = True

print(chrome.__dict__)  # class variable is not present
print(firefox.__dict__)  # class variable is not present

print(chrome.connected)
print(firefox.connected)