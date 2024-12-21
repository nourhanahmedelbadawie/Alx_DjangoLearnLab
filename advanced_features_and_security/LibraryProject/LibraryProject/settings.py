AUTH_USER_MODEL = 'bookshelf.CustomUser'
DEBUG = False  # Never set DEBUG to True in production
SECURE_BROWSER_XSS_FILTER = True  # Prevents some types of cross-site scripting (XSS) attacks
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking by disallowing the page to be embedded in an iframe
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents browsers from interpreting files as something else (e.g., executing JavaScript)
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
# DO NOT do this! Direct string formatting is dangerous
query = f"SELECT * FROM books WHERE title = '{user_input}'"

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-scripts.com')
CSP_STYLE_SRC = ("'self'", 'https://trusted-styles.com')
CSP_IMG_SRC = ("'self'", 'https://trusted-images.com')

CSP_BLOCK_ALL_MIXED_CONTENT = True  # Prevents mixed-content (HTTP and HTTPS)
