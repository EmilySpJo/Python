# film_selector
**Note: This is a Personal Project**
## Project purpose
<p>Whether its individual browsing or trying to find something to watch as a family, I have found that hours a week are wasted scrolling through Netflix or Amazon Prime in an attempt to find something that fits the genre, platform and format we want.<br><br>In an attempt to solve this dilemma, I have created an interface which allows the user to input their preferred platform, genre and media type and then uses these parameters to suggest 3 possible shows or films. The user can reset these choices as many times as they wish until they get a suggestion of interest. </p>


## Approach
<p>I have taken big data sets listing the shows and films available on both netflix and amazon prime from kaggle and then altered them, removing columns, creating new sub-datasets, etc to suit the needs of the system.</p>

[Click to view data sets](./data/)

### Scripts:
|Script name | script role | reference |
|------------|-------------|-----------|
|gui.py| This script implements the GUI with which the user interfaces. It enables the user to select a platform, media type and genre |[script](./gui.py)|
|get_suggestions_functions.py| This script contains the data handling function which iterates through the relevant csv, as determined by the users selected platform, media and genre and subsequently selects 3 films or TV shows which it returns as suggestions|[script](./get_suggestions_functions.py)|


## Proof of concept:
The below images correspond to version 2 of the system
##### Decision input screen
![Input screen](./images/example%20outputs/home_page.png)
##### Suggestion output
![suggestion_pop_up](./images/example%20outputs/suggestion_screen_1.png)
##### Suggestion consolidation
![suggestion_consolidation](./images/example%20outputs/final_suggestion_screen.png)

## Improvements
From here I would like to make the following improvements:
- Add overall 'Surprise me' functionality -> this would randomly select a platform, media type and corresponding genre
- Add isolated 'Surprise me' functionality -> user could make some decisions but others could be randomly selected
- GUI improvement -> perhaps make the buttons / Comboboxes more visually appealing

## Resources used
|Resource | Use | Example |
|---------|-----|---------|
|tkinter |tkinter is the predominant library used to create the GUI |[GUI script](./gui.py)|
|Jupyter notebooks<br> pandas| I imported the python pandas library within a jupyter notebook for both the Amazon Prime and Netflix data sets to facilitate efficient data handling.|[Data handling](./data/)|
