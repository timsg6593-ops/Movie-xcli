import requests
from bs4 import BeautifulSoup

class BoredflixAPI:
    BASE_URL = 'https://www.boredflix.com'
    
    def search_movies(self, query, limit=5):
        response = requests.get(
            f"{self.BASE_URL}/search", 
            params={'query': query}
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        

        results = []
        for item in soup.select('.movie-card')[:limit]:
            results.append({
                'id': item['data-id'],
                'title': item.find('h3').text,
                'year': item.find(class_='year').text
            })
        return results

    def get_trending(self, days=7):
        response = requests.get(f"{self.BASE_URL}/trending/{days}")

        
    def get_movie_url(self, movie_id):

        response = requests.get(f"{self.BASE_URL}/movie/{movie_id}")
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('video')['src']
