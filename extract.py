from bs4 import BeautifulSoup

# Open a html file manually downloaded from the url generated by main.py for reading
# encoding = 'utf-8' is a type of variable-length character encoding standard used for webs
with open('assets/bookingdotcom_philadelphia.html', 'r', encoding='utf-8') as f:

    # read the entire contents of the html file
    contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")
    
    # Get each hotel's property card contents from HTML
    with open('hotels.txt', 'w', encoding='utf-8') as file:
        # each hotel property card container has attribute data-testid = 'property-card-container'
        for container in soup.find_all('div', {'data-testid': 'property-card-container'}):
            file.write(str(container) + '\n\n')

            title = container.find('div', {'data-testid': 'title'}).text
            rating = container.find('div', {'class': 'a3b8729ab1 d86cee9b25'}).text[0:3]

            print(f"Hotel: {title}\tRating: {rating}")
