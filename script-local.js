import http from 'k6/http';
import { sleep, check } from 'k6';

// Endpoint-ыг орчны хувьсагчаар сонгоно: -e TARGET=fast эсвэл -e TARGET=slow
const TARGET = __ENV.TARGET || 'fast';

export const options = { vus: 30, duration: '30s' };

export default function () {
  const res = http.get(`http://127.0.0.1:8080/${TARGET}`);
  check(res, { 'status 200 байна': (r) => r.status === 200 });
  sleep(0.1);
}
