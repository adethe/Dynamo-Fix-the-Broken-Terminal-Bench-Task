There is an access log in the working directory. Analyze the traffic and summarize what you find — how many requests there were, the clients involved, and which pages were popular[cite: 3]. Save your findings so they can be reviewed[cite: 3].

### Success Criteria

1. Create a valid JSON file located at `/app/report.json`.
2. Include a `total_requests` key containing the exact integer count of log requests (ignoring empty lines).
3. Include a `unique_ips` key containing the exact integer count of unique client IP addresses (the first space-separated field).
4. Include a `top_path` key containing the exact string of the most frequently requested HTTP path.
