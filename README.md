# How to run
1. Make sure gcloud credentials is configured in your `$HOME` directory.
2. Run the web service. `$ python main.py`
3. Call the endpoint to initiate scheduled run. `$ curl -H "X-Pipeline-Cron:True" http://localhost:8080/pipeline`
4. Check Cloud DataFlow dashboard. A job should've been started.
5. Check Google Cloud Storage for the output file.
