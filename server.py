from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

from src.calculator import Calculator


calculator = Calculator()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._send(200, {"status": "healthy", "service": "calculator"})
            return

        if parsed.path == "/api/calc":
            try:
                qs = parse_qs(parsed.query)
                a = float(qs.get("a", ["0"])[0])
                b = float(qs.get("b", ["0"])[0])
                op = qs.get("op", [""])[0]

                result = calculator.calculate(op, a, b)
                self._send(200, {"a": a, "b": b, "op": op, "result": result})
            except Exception as e:
                self._send(400, {"error": str(e)})
            return

        self._send(404, {"error": "not found"})

    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()