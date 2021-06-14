
# Overview

Sustainable seafood web app where users can search, discover, and save sustinable fish by their location. 
--------
Users input zip code and can search the name of a fish and return information about it's sustinability, including: Location, Population Status, Avaliability, Environmental Considerations, Farming Methods, Human Health, an image of the fish. Will also use zip code to recommend nearby farmer's markets and more sustainable fish options. 

Users should be able to search by fish, but also location, which returns a list of sustainable fish for their location. 

### Technologies required (besides typical Hackbright tech stack)

Fish Watch API, Farmer's Market API, Twilio (maybe)

### Stored Data

User: email, password, zip code (optional), fish name, favorited fish, phone number (optional)

### Fetched Data
Fish: name, alternative names, picture, habitat impact, NOAA Fisheries Region, population status, environmental considerations
Farmers market: by zip code & those that sell fish

### Roadmap

#### MVP

- Users can create an account and login
- display fish name, image, sustainability status
- Users can save fish to their favorites
- Users can filter by status and region 
- Users can search by fish name 
--- autocomplete dropdown - jQuery autocomplete 

#### 2.0

- Users can see nearby farmer's markets that sell fish
- Pretty and interactive UI
--- bootstrap & mobile
- Clean up HTML tags in API response // did this with "|safe"
- Keep boxes checked 
AJAX w/o page load or generally html in res that has elements already selected

#### 3.0

- Twilio: Users can text themselves their saved fish list
- Cloudflare/ download, store, resize images
----check if image is in static folder, if not, download to static. When image is served, check if in static, if so, serve that version. 
- jQuery loading at once
-- loading spinner
- fish animation on profile page
--- sort by most popular, what cool data can we pull, trends page
-----map bubbles 


### Notes
Species:
- Process to paginate all species page?
element that only displays # of containters. on next click, render next 10/delete previous 10


-----
- HTML, CSS, JS quiz
- Add spiner while page loads
- Make it pretty
- Testing, writing tests
- Responsive design/mobile
- fix secrets stuff / twilio environ 
