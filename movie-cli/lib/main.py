import argparse
from boredflix_api import BoredflixAPI
from downloader import download_movie
from player import play_stream

def main():
    parser = argparse.ArgumentParser(
        description='movie-cli: Streaming-Tool für Boredflix.com'
    )
    
    subparsers = parser.add_subparsers(dest='command')


    search_parser = subparsers.add_parser('search', help='Suche Filme')
    search_parser.add_argument('-q', '--query', required=True, help='Suchbegriff')
    search_parser.add_argument('-l', '--limit', type=int, default=5,
                              help='Anzahl der Ergebnisse')


    trending_parser = subparsers.add_parser('trending', 
        help='Zeige Top-Trending-Filme'
    )
    trending_parser.add_argument('-d', '--days', type=int, default=7,
                                help='Trending-Zeitraum (Tage)')


    download_parser = subparsers.add_parser('download',
        help='Film herunterladen (MP4)'
    )
    download_parser.add_argument('-i', '--id', required=True, 
                              help='Filme-ID')
    download_parser.add_argument('-o', '--output', default='./data/',
                               help='Speicherort')


    play_parser = subparsers.add_parser('play',
        help='Film im VLC-Player streamen'
    )
    play_parser.add_argument('-i', '--id', required=True, 
                           help='Filme-ID')
    
    args = parser.parse_args()
    api = BoredflixAPI()

    if args.command == 'search':
        results = api.search_movies(args.query, args.limit)
        for movie in results:
            print(f"{movie['id']} | {movie['title']} ({movie['year']})")
            
    elif args.command == 'trending':
        trending = api.get_trending(days=args.days)
        for idx, movie in enumerate(trending[:10], 1):
            print(f"{idx}. {movie['title']} - Views: {movie['views']}")
    
    elif args.command == 'download':
        url = api.get_movie_url(args.id)
        download_movie(url, args.output)
        
    elif args.command == 'play':
        url = api.get_movie_url(args.id)
        play_stream(url)

if __name__ == '__main__':
    main()
