from flask import Flask, request, jsonify
from instagpy import InstaGPy

app = Flask(__name__)
insta = InstaGPy()

@app.route("/api/instagram-user")
def instagram_user():
    username = request.args.get("username", "").strip()
    
    if not username:
        return jsonify({"error": "Brak nazwy użytkownika"}), 400
    
    try:
        user = insta.get_user_basic_details(username, pretty_print=False)
        if not user:
            return jsonify({"error": "Nie znaleziono użytkownika"}), 404
        
        data = {
            "id": user.get("id"),
            "username": user.get("username"),
            "full_name": user.get("full_name"),
            "follower_count": user.get("follower_count"),
            "following_count": user.get("following_count"),
            "media_count": user.get("media_count"),
            "is_private": user.get("is_private"),
            "is_verified": user.get("is_verified")
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
