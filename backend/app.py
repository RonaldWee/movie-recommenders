from flask import Flask, request, jsonify
from recommender import models, get_recommendations

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = int(request.args.get("user_id"))
    algo_name = request.args.get("algo", "SVD")

    model = models.get(algo_name)
    if not model:
        return jsonify({"error": f"Algorithm '{algo_name}' not found."}), 400

    recommendations = get_recommendations(user_id, model=model)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
