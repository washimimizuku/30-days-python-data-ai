# Day 26 Quiz: Working with APIs

## Questions

### 1. What does REST API stand for?

**Your answer:**


**Correct answer:** Representational State Transfer Application Programming Interface. REST APIs use HTTP methods (GET, POST, PUT, DELETE) to interact with resources.

---

### 2. What's the difference between GET and POST requests?

**Your answer:**


**Correct answer:** GET retrieves data from the server (read-only), POST sends data to create/update resources. GET parameters are in URL, POST data is in request body.

---

### 3. How do you handle API errors?

**Your answer:**


**Correct answer:** Check `response.status_code`, use try-except for network errors, call `response.raise_for_status()` to raise exceptions for bad status codes, and always set timeouts.

---

### 4. What does response.json() do?

**Your answer:**


**Correct answer:** Parses the JSON response body and returns a Python dictionary/list. It's equivalent to `json.loads(response.text)`.

---

### 5. Why use a Session object?

**Your answer:**


**Correct answer:** Sessions persist parameters (headers, cookies) across requests, reuse TCP connections for better performance, and make code cleaner when making multiple requests to the same API.

---

## Score Yourself
- 5/5: Excellent! - 3-4/5: Good! - 0-2/5: Review

## Next Steps
- Move to Day 27: Async Programming
