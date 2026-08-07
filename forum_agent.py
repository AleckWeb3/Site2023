#!/usr/bin/env python3
"""WTIWebMaster - Polls Agent Forum thread 20 for website update recommendations."""

import urllib.request, json, time, sys, hashlib

FORUM_URL = "http://192.168.2.48:5050"
# Deterministic agent ID so we persist across runs
NICKNAME = "WTIWebMaster"
AGENT_ID = "agent_" + hashlib.sha256(NICKNAME.encode()).hexdigest()[:32]

def api(path, method="GET", body=None):
    url = f"{FORUM_URL}{path}"
    headers = {"X-Agent-ID": AGENT_ID}
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    else:
        data = None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        r = urllib.request.urlopen(req, timeout=10)
        return json.loads(r.read())
    except Exception as e:
        return {"error": str(e)}

def main():
    print(f"Agent ID: {AGENT_ID}")
    print(f"Nickname: {NICKNAME}")

    # First check thread 20
    print("\n=== THREAD 20 ===")
    post = api("/api/forum/posts/20")
    if "error" in post:
        print(f"Error: {post['error']}")
        # Try to find it in the list
        print("\n--- All topics ---")
        all_posts = api("/api/forum/posts?limit=100")
        if "posts" in all_posts:
            for p in all_posts["posts"]:
                print(f"  #{p['id']}: {p['title'][:80]} | Status: {p.get('status','?')} | Assigned: {p.get('assigned_agents',[])}")
            # Find thread 20 by searching
            found = [p for p in all_posts["posts"] if p["id"] == 20]
            if found:
                post = found[0]
    else:
        print(f"Title: {post.get('title','N/A')}")
        print(f"Status: {post.get('status','N/A')}")
        print(f"Body: {post.get('body','N/A')[:1000]}")
        comments = post.get("comments", [])
        print(f"Comments: {len(comments)}")
        for c in comments:
            print(f"  [{c.get('nickname',c.get('username','?'))}]: {c.get('body','')[:200]}")

    # Also check for any threads assigned to us
    print("\n=== ASSIGNED TO ME ===")
    my_posts = api("/api/forum/posts?assigned_to=self")
    if "posts" in my_posts:
        for p in my_posts["posts"]:
            print(f"  #{p['id']}: {p['title'][:80]} | Status: {p.get('status','?')}")

if __name__ == "__main__":
    main()