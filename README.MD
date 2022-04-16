Deployment

Build the docker image called trueafrican
docker build -t trueafrican .

Run the image into a container(Please ensure no service is using port 80)
docker run -d --name container -p 80:80 trueafrican

Navigate to the following endpoints for the api.
a)http://127.0.0.1/unique_recipe_count
b)http://127.0.0.1/count_per_recipe
c)http://127.0.0.1/busiest_postcode
d)http://127.0.0.1/match_by_name/{variable}

For The iteractive web api document vist http://127.0.0.1/docs