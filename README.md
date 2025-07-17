CERINTE
Aplicație de automatizare folosind Selenium
    Automatizare creare, multiplicare și trimitere formulare feedbac în Microsoft Forms
    Monitorizare prețuri pe site-uri cu content dinamic (ex. Emag)
    Transmitere mesaje mai multor utilizatori/teamuri în Microsoft Teams
    Crearea unui feed cu post-uri de pe social media
    Trimiterea unor prompt-uri către diverse LLM-uri și obținerea de răspunsuri fără API


Proiectul urmareste crearea unei aplicatii capabile sa ofere utilizatorului tool-urile necesare pentru a putea automatiza cerintele de mai sus.
Un aspect foarte important il reprezinta chromedriver.exe, care trebuie sa aiba neaparat aceeasi versiune cu chrome-ul de pe dispozitivul pe care ruleaza (https://googlechromelabs.github.io/chrome-for-testing/).In caz contrar, trebuie schimbat cu o noua versiune.
Fisierul browser.py contine setarile pentru chrome

Pentru monitorizare, aplicatia are nevoie de link-ul produsului de pe emag
In fisierul config.py se pot modifica persoanele si mesajul care sa le fie trimis
Feed-ul este creat pe baza aplicatiei X(actualul Twitter), unde trebuie specificat numarul de postari pe care sa le preia
Conversatia cu chatGPT-ul are loc doar daca este deschisa pagina de chrome in paralel(nu merge headless)

