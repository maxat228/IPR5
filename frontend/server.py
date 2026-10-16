from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import urllib.error

BACKEND = "http://backend-service:8080"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            try:
                with urllib.request.urlopen(BACKEND + self.path) as resp:
                    body = resp.read()
                self._send(200, "application/json; charset=utf-8", body)
            except urllib.error.HTTPError as e:
                body = e.read()
                self._send(e.code, "application/json; charset=utf-8", body)
            except Exception as e:
                self._send(500, "text/plain; charset=utf-8", str(e).encode("utf-8"))
            return

        try:
            with open("index.html", "rb") as f:
                body = f.read()
            self._send(200, "text/html; charset=utf-8", body)
        except Exception:
            self._send(404, "text/plain; charset=utf-8", b"not found")

    def _send(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()