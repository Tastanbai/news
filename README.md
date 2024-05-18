
# News Project

This is a Django-based news project with the following features:
- List of news articles with tags.
- Detailed view for each news article.
- News articles can be filtered by tags.
- News view count and statistics page.
- Like and dislike functionality for news articles.
- REST API for getting, creating, and deleting news articles.
- Infinite scrolling to load more news articles without page reload.
- User authentication for liking and disliking articles.

## Features

- **News List**: Display a list of news articles with infinite scrolling.
- **News Detail**: View detailed information about a news article.
- **News by Tag**: Filter news articles by tags.
- **News Statistics**: View statistics of news views.
- **Like/Dislike**: Like and dislike news articles with real-time updates.
- **Admin Panel**: Manage news articles and tags via Django admin.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/news_project.git
    cd news_project
    ```

2. **Create and activate a virtual environment**:
    - Windows:
        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```
    - macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser** (follow the prompts to set username and password):
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    - Open your web browser and go to `http://127.0.0.1:8000/` to view the news list.
    - Go to `http://127.0.0.1:8000/admin/` to access the admin panel and manage news articles and tags.

## Usage

- **News List**: The homepage displays a list of news articles. Scroll down to load more articles.
- **News Detail**: Click on a news article title to view its details, tags, and like/dislike options.
- **News by Tag**: Click on a tag to filter news articles by that tag.
- **News Statistics**: Access the statistics page to view the most viewed news articles.
- **Like/Dislike**: Like or dislike a news article. The like count updates in real-time.

## API Endpoints

- **Get News List**: `GET /api/news/`
- **Create News Article**: `POST /api/news/`
- **Delete News Article**: `DELETE /api/news/{id}/`
- **Like News Article**: `POST /api/news/{id}/like/`
- **Dislike News Article**: `POST /api/news/{id}/dislike/`

## Folder Structure

```
news_project/
│
├── news/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   ├── templates/
│   │   ├── news/
│   │   │   ├── news_list.html
│   │   │   ├── news_detail.html
│   │   │   ├── news_by_tag.html
│   │   │   ├── news_statistics.html
│   ├── __init__.py
│   ├── admin.py
│   ├── api_views.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── news_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We appreciate any contributions, whether they are bug fixes, new features, or improvements to the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- REST framework Documentation
