import json
import requests

def fetch_reviews_for_key(key):
    source = f"https://ratings-api.udacity.com/api/v1/reviews?node={key}&limit=5000&page=1"
    r = requests.get(source)
    return r.json()

with open("./data/degrees.json", "r") as data_file:
    degrees = json.load(data_file)
    
    print("start fetching reviews")

    output_data = []
    for degree in degrees:
        key = degree.get("key")
        data = fetch_reviews_for_key(key)
        
        print("key: " + key)
        
        ratings = {
          "average_rating": data["nd_avg_rating"],
          "count": data["count"],
          "stats": data["stats"]  
        }

        sample = {
          **degree,
          **ratings
        }

        output_data.append(sample)
    
    print("processed job")
    with open("./data/processed.json", "w+") as output:
        output.write(json.dumps(output_data, indent=2))
        print("job has been finished")