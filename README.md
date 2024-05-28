## Python Flask Application Design

### HTML Files

- **main.html:**
   - This will be the main HTML page for the application.
   - It will contain the necessary HTML structure, including elements to display the news articles.

### Routes

- **@app.route('/')**:
   - This route will be used to display the main page of the application.
   - It will render the main.html template and pass any necessary data to it.

- **@app.route('/news-articles')**:
   - This route will be used to fetch and display news articles.
   - It will use a web scraping library or an API to retrieve the news articles and render a template with the collected data.

- **@app.route('/article/<int:article_id>')**:
   - This route will be used to display a specific news article.
   - It will fetch the article based on the provided article ID and render a template with the article's details.