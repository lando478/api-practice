# flask is the server that runs the api. 

from flask import Flask, request, jsonify

# root is an endpoint on the server. 
# HTTP is how we communicate data over the internet
# There is GET, POST, PUT, DELETE, etc.
app = Flask(__name__)

# here we used a path parameter. 
# query parameters are another way to pass data to an endpoint.we use a ? to start the query parameters. its just additional varaibles. 
@app.route("/get-user/<user_id>")
def get_user(user_id):
      user_data = {
            "user_id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com"
      }
      extra = request.args.get("extra")
      if extra:
            user_data["extra"] = extra
      return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
      # if request.method == "POST":
      data = request.get_json()
      return jsonify(data), 201
            

if __name__ == '__main__':
    app.run(debug=True)
