from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import time


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep-alive: k6 дахин дахин шинэ холболт нээхгүй

    def do_GET(self):
        if self.path == "/fast":
            body = b"fast ok\n"
        elif self.path == "/slow":
            time.sleep(0.1)  # 100 мс зориудаар удаашруулна
            body = b"slow ok\n"
        else:
            self.send_response(404)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # терминалыг лог дүүргэхээс сэргийлнэ


if __name__ == "__main__":
    print("Сервер http://127.0.0.1:8080 дээр ажиллаж байна (зогсоох: Ctrl+C)")
    ThreadingHTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
