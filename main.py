from flask import Flask
from google.cloud import storage
import csv
import io

app = Flask(__name__)

@app.route("/")
def read_csv():
    bucket_name = "my_bucket_anirutth"
    file_name = "anirutth_data.csv"

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    csv_data = blob.download_as_text()

    output = []
    reader = csv.reader(io.StringIO(csv_data))
    for row in reader:
        output.append(", ".join(row))

    return "<br>".join(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
