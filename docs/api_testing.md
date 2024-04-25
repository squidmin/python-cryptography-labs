# API testing

You can use `curl` to test the encryption and decryption endpoints.
Below are the commands for interacting with each endpoint, assuming the server is running locally on port 8000.

### Encrypt Endpoint

To encrypt plaintext, send a POST request with the plaintext in the body of the request:

```bash
curl -X POST "http://127.0.0.1:8000/encrypt/" \
-H "Content-Type: application/json" \
-d "{\"plaintext\":\"Hi there\"}"
```

The server should respond with JSON data that includes the `ciphertext`, `iv` (initialization vector), and `key`, all of which are needed for decryption.

### Decrypt Endpoint

To decrypt the ciphertext, you need the ciphertext, the IV, and the key from the encryption response.
Replace `<CIPHERTEXT>`, `<IV>`, and `<KEY>` in the command below with actual values received from the encryption endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/decrypt/" \
-H "Content-Type: application/json" \
-d "{\"ciphertext\":\"<CIPHERTEXT>\", \"iv\":\"<IV>\", \"key\":\"<KEY>\"}"
```

This command sends a request to the `/decrypt/` endpoint with a JSON payload containing the ciphertext, IV, and key.
The server should respond with JSON data that includes the decrypted `plaintext`.

### Example Flow

1. **Encrypt a message:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/encrypt/" \
   -H "Content-Type: application/json" \
   -d "{\"plaintext\":\"Hi there\"}"
   ```

   Response might be:
   ```json
   {
       "iv": "some_iv_value",
       "ciphertext": "some_ciphertext_value",
       "key": "some_key_value"
   }
   ```

2. **Decrypt the message using the response from the encrypt step:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/decrypt/" \
   -H "Content-Type: application/json" \
   -d "{\"ciphertext\":\"some_ciphertext_value\", \"iv\":\"some_iv_value\", \"key\":\"some_key_value\"}"
   ```

   The response should give you:
   ```json
   {
       "plaintext": "Hi there"
   }
   ```

These commands allow you to fully test encryption and decryption services using `curl`.
You can also try importing the commands to Postman.
