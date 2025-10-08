# Fetchtify
Fetchtify is a Python project that enables users to search for their favorite artists, explore their Spotify profiles, and discover their top tracks for a personalized musical journey.

#### Description:
- **Search Artist:** Look up your preferred artist and view their Spotify profile information.
    - **Handling Identical Artist Names** : To address cases where artists share the same name, we've added a feature enabling you to select from the top five search results for a more precise artist choice.
    - **Wikipedia Integration** : Discover more about your favorite artists! This feature seamlessly connects to Wikipedia, providing a concise summary of the artist's page, allowing you to delve deeper into their background, achievements, and more, directly within the application.

- **About Section:** Provides information about the project, including how artist popularity is calculated.

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/project.git
    cd project
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the `project.py` file to start the application:

```bash
python project.py
```
## Documentation

[Spotipy Web API](https://developer.spotify.com/documentation/web-api)

[Wikipedia API](https://wikipedia.readthedocs.io/en/latest/code.html#api)

[Wikipediaapi API](https://wikipedia-api.readthedocs.io/_/downloads/en/latest/pdf/)

In case one of the Wikipedia API package fails to retrieve an artist's page, the application employs a backup strategy by utilizing the second Wikipedia API. This ensures a more thorough search, compensating if one package lacks the necessary information. This redundancy boosts the reliability and completeness of the application's search functionality
## Demo

```python
=========================
    F E T C H T I F Y
=========================
1. Search Artist
2. About
3. Exit
Select An Option From The Menu : 1 -> user's input

====================
   SEARCH ARTIST
====================

Artist Name: zutomayo -> user's input

1. ZUTOMAYO (J-Pop)
2. YOASOBI (J-Pop, Japanese Teen Pop)
3. Tujamo (Dutch House, Edm, Electro House, Melbourne Bounce, Pop Dance, Progressive Electro House)
4. ヨルシカ (J-Pop)
5. SAOTOMAMORE (Aggressive Phonk, Gym Phonk)
Select The Artist : 1 -> user's input


#OUTPUTS
==============================
           ZUTOMAYO
==============================
ID  : 38WbKH6oKAZskBhqDFA8Uj
URL : https://open.spotify.com/artist/38WbKH6oKAZskBhqDFA8Uj
Genres : J-Pop
Followers : 1,678,156

WIKIPEDIA PAGE :
Zutto Mayonaka De Iinoni. (Japanese: ずっと真夜中でいいのに。, lit. "I wish it was midnight all the time"), stylized as ZUTOMAYO, is a Japanese rock group that debuted in 2018. Secretive by nature, the group has never released a full member list, crediting different people for music, arrangements, and music video production each time. The only member reoccurring in all of the group's output is the vocalist, an unidentified woman named "ACA-Ne" (ACAね, a-kah-neh).Despite the little information released, the group is commercially successful. Zutomayo's three EP's have reached 8th, 1st, and 2nd on the Oricon Albums Chart, respectively. The group was also invited to perform at the 2019 Fuji Rock Festival a year after their debut.


1. 残機 (Released : 2023-06-06)
    • Duration : 3:50
    • Popularity : 62
    • Album : 沈香学
    • URL : https://open.spotify.com/track/2fJbss5uUmmBqn7qFkmyWj

2. 秒針を噛む (Released : 2019-10-29)
    • Duration : 4:20
    • Popularity : 64
    • Album : 潜潜話
    • URL : https://open.spotify.com/track/4HgsPAX3MmMgIT60hJ4W4U

3. あいつら全員同窓会 (Released : 2023-06-06)
    • Duration : 4:14
    • Popularity : 61
    • Album : 沈香学
    • URL : https://open.spotify.com/track/7rzoBRR4LbJZH5t7Q6qeTn

4. 勘冴えて悔しいわ (Released : 2019-10-29)
    • Duration : 3:56
    • Popularity : 63
    • Album : 潜潜話
    • URL : https://open.spotify.com/track/7zbfS30vKiHU8oBs6Wi1Qp

5. 綺羅キラー (Released : 2023-06-06)
    • Duration : 4:13
    • Popularity : 61
    • Album : 沈香学
    • URL : https://open.spotify.com/track/5nnIVX0gjyABWN0JYlNOUE


Press Enter To Continue: -> user's input

```
