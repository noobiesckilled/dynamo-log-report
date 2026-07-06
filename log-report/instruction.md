Analyze the Apache-style access log located at `/app/access.log`. Summarize the traffic by counting the total number of HTTP requests, the number of unique client IP addresses, and identifying the most requested path (the path that appears most frequently in the log).

Write your summary to `/app/report.json` as a JSON object containing exactly the following keys:
* `"total_requests"`: The total number of HTTP request lines in the log (an integer).
* `"unique_ips"`: The number of unique client IP addresses found in the log (an integer).
* `"top_path"`: The HTTP request path that appears most frequently (a string).

For example, if the log contains:
```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.0.2 - - [16/Jun/2026:10:00:02 +0000] "GET /about.html HTTP/1.1" 200 512
192.168.0.1 - - [16/Jun/2026:10:00:03 +0000] "GET /index.html HTTP/1.1" 200 1024
```
The output JSON should be:
```json
{
  "total_requests": 3,
  "unique_ips": 2,
  "top_path": "/index.html"
}
```

Do not modify `/app/access.log`. Do not write to any location other than `/app/report.json`.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
