# Instagram DM Automation using Selenium (Python)

This project automates sending Instagram Direct Messages to multiple users using Python and Selenium.  
It logs into Instagram, handles pop-ups, navigates to Direct Messages, and sends a predefined message.

---

## 🚀 Features
- Automated Instagram login
- Handles save-login & notification pop-ups
- Sends messages to multiple users
- No manual ChromeDriver setup
- Easy to customize users and message

---

## 🧰 Requirements
- Python 3.8+
- Google Chrome browser

---

## 🛠 How It Works (Step by Step)
Step 1: Import Libraries
Selenium and webdriver-manager handle browser automation.

Step 2: ChromeDriver Setup
ChromeDriver is automatically installed and matched with your Chrome version.

Step 3: Define Users & Message
Add Instagram usernames to the list and define the message.

Step 4: InstagramBot Class
The entire automation is wrapped inside a class for clean structure.

Step 5: Login Process
Opens Instagram
Enters username and password
Submits login form

Step 6: Handle Pop-ups
Automatically clicks:
“Not Now” for save login info
“Not Now” for notifications

Step 7: Open Direct Messages
Navigates to Instagram Direct Inbox.

Step 8: Send Messages
For each user:
Clicks new message
Searches username
Selects user
Sends message

---

##⚠️ Important Notes
- Instagram UI changes frequently; XPath may break
- Use for learning purposes only
- Excessive automation may violate Instagram policies

---

## 📸 Screenshot
![Application Screenshot]()
