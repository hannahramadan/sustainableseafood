    // Get's market ID and name by zip code
    function getMarkets(zip) {
        $.ajax({
            type: "GET",
            contentType: "application/json; charset=utf-8",
            url: "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=" + zip,
            dataType: 'jsonp',
            success: function searchResultsHandler(data) { 
                for (key in data) { //key is our 'results'
                    let results = data[key]; //results is our list of objects
                    for (let i = 0; i < 5; i++) {
                        let result = results[i]; //result is 1 object
                        marketid = result["id"]
                        marketname = result["marketname"]
                        getDetails(marketid, marketname)
                    }
                }
            }
        });
    }

    // Handles the market IDs. Provides details on each marketplace 
    function getDetails(marketid, marketname) {
        let marketplaces = $('#marketplaces')
        $.ajax({
            type: "GET",
            contentType: "application/json; charset=utf-8",
            url: "http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id=" + marketid,
            dataType: 'jsonp',
            success: function detailResultHandler(detailresults) {
                for (key in detailresults) {
                    let results = detailresults[key];
                    let googleLink = results['GoogleLink']
                    let address = results['Address']
                    // let products = results['Products']
                    // let schedule = results['Schedule']
                    addMarketsToProfile(marketplaces, googleLink, marketid, marketname,address)
                }
            }
        });
    }
    // Adds marketplaces and their map links to the DOM
    function addMarketsToProfile(marketplaces, googleLink, marketid, marketname, address){
        marketplaces.append('<a href="'+googleLink+'"target="_blank"><li id='+marketid+' value='+marketid+'>'+marketname+'</li></a><ul><li>'+address+'</li></ul>')
    }
