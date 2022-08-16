# Testimonial victims API-REST

REST API with NER atributes of victim's testimonies from Cuando los pájaros no cantaban. 
This is the Truth Comission's report with some testimonies of colombian armed conflict's victims.

## Technologies

* Mongo Atlas for DB
* Python language
* FastAPI framework
* Azure Cognitive Search for NER atributes (people, locations, organizations and key words)
* Azure Web Service and Git Actions for continuous deployment (CD)  

## Use

You can see it deployed in Azure Web [here](http://testimoniesreport.azurewebsites.net/). 

Select a GET method, click on <kbd>Try it out</kbd> and <kbd>Execute</kbd>! 

You can consume it with Postman too, or with Power BI for analytics like [this](https://youtu.be/FuGZoRkRmyI?t=64).

### With CLI

Make sure you have `curl` and `jq` packages.

```
curl -X 'GET' 'http://testimoniesreport.azurewebsites.net/testimonios/6?organizations=false&keyWords=false' | jq .
```

