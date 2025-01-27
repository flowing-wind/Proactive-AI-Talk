# Proactive AI Talk  ![Static Badge](https://img.shields.io/badge/side_project-%23ff9300)

![Static Badge](https://img.shields.io/badge/python-3.12-blue) ![Static Badge](https://img.shields.io/badge/platforms-Windows_Linux-%2302dbf0) ![Static Badge](https://img.shields.io/badge/contributions-welcome-green) ![Static Badge](https://img.shields.io/badge/I_speak-English_Chinese-%23ed02ba)

AI will "get" news from the Internet and start a conversation with you.

#### Table of Contents
- [Proactive AI Talk](#proactive-ai-talk)
  * [About](#about)
  * [Demo](#demo)
  * [Usage](#usage)
  * [Directory Tree](#directory-tree)
  * [Contributing](#contributing)
    + [Scraper](#scraper)
  * [License](#license)

## About
This project uses a web scraper to gather news/articles from various websites and feed them into AI models, along with appropriate  prompts to instruct them to generate topics and initiate a conversation.

## Demo
**This is an example using DeepSeek API to chat with.  **

The number of rounds you want to chat with the AI: 3

AI: Hey! So, Nvidia just dropped their new RTX 5090, and it’s a beast for 4K gaming. It’s got this crazy DLSS 4 tech that can boost frame rates like crazy, but it’s also $1,999 and sucks up a ton of power. What do you think—worth the hype, or is it just overkill for most gamers?

User: Oh, I won't buy that anyway. My RTX3060 is enough for most of the games I play. To be honest, it would be a waste if a student like me uses it to play games.

AI: Yeah, totally get that! The RTX 3060 is solid for most games anyway, and the 5090 feels like overkill unless you're deep into 4K or heavy AI workloads. Plus, that price tag is wild for gaming, especially if you're a student. What games are you playing these days? Anything pushing your 3060 to its limits?

User: Yeah, Nvidia today focuses more on AI, some old GPUs are enough for gaming. But you know, the 3A game Black Myth: Wukong consumes a lot on GPU, my RTX 3060 felt some pressure and I had to lower the graph quality.

AI: Oh, Black Myth: Wukong is such a stunning game, but yeah, it’s a beast on GPUs. Even the RTX 5090 struggles a bit without DLSS! Lowering settings is totally fair—it’s still a gorgeous game even on medium. Have you tried using DLSS or FSR on your 3060? It might help squeeze out some extra performance without sacrificing too much quality. What’s your favorite part of the game so far?


## Usage
1. Clone this repositories.
   ```bash
   git clone https://github.com/flowing-wind/Proactive-AI-Talk.git
   ```
2. Install necessary libraries.
   ```bash
   pip install -r requirements.txt
   ```
3. Create a new file `api_key.txt` in the root directory of the project and fill in the API key of your model.
4. Run `init.py` and this will create a `db` file in `Web_Scraping`.
   ```bash
   python init.py
   ```
5. Run `api.py`, input the rounds you want to chat and begin the talk.
   ```bash
   python api.py
   ```

## Directory Tree
```
.
├── Web_Scraping/
│   ├── TheVerge/
│   │   ├── __init__.py
│   │   └── theverge.py
│   ├── links.db
│   └── sources.json
├── LICENSE
├── README.md
├── requirements.txt
├── Message_Generator.py
├── api_key.txt
├── api.py
└── init.py
```
## Contributing
Contributions of any kind are welcome! Feel free to submit issues and open PRs!  

If you want to add more web scrapers, put your own `.py` file in `Web_Scraping/Your scraper` and create a blank `__init__.py` to ensure it can be recognized as a module, then open `sources.json` to add your module path:   

```json
"YourScraper": "path_to_your_py_file"
```
For example, if your `.py` file path is `Web_Scraping/TheVerge/theverge.py`, then your `path_to_your_py_file` is `Web_Scraping.TheVerge.theverge`  

### Scraper
To be compatible with this program, in general, you should define two functions in your `.py` file:  
1. `YourScraper_init()`
   This function is called in `init.py`, and is responsible for searching (e.g. search the main page) and adding news links to the database.  
   When adding links to the database, the `source` column should match the `YourScraper` in json file, for the program will import corresponding `GetContent` function according to the `source` in database and get the function through json.
2. `GetContent(link)`
   The function name is designed to be the same across all scrapers for better invocation and management. It is mainly used to scrape news/articles from the links gathered before and return the passage.
## License
  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
