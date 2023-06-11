# japan_shop
Django first project<br>    
Little internet-shop with authenctication, cart and favorites.

If you want to run this project, you need to follow next steps:
1. Install all requirements >>> pip install -r requirements.txt
2. Create .env file in japan_shop folder and append there next code:      
EMAIL_HOST_USER=yourValidGmailAddress    
EMAIL_HOST_PASSWORD=gmailAppPassword*      
3. If you want to login with Google you need to run server with https protocol with help of next command    
python manage.py runserver_plus --cert-file cert.crt      
*See more information about App Password here https://support.google.com/accounts/answer/185833?hl=ru <br>

Admin login: admin    
Admin password: admin

