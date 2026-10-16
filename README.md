# 📚 FastAPI Full-Stack Learning Project: From Scratch to Production

[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0_Async-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-red?style=for-the-badge)](https://alembic.sqlalchemy.org/)
[![AWS S3](https://img.shields.io/badge/AWS-S3_Storage-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/s3/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![UV](https://img.shields.io/badge/UV-Package_Manager-DE5FE9?style=for-the-badge)](https://docs.astral.sh/uv/)
[![Pytest](https://img.shields.io/badge/Tested_with-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)

> **A comprehensive full-stack practice project built from the ground up to master modern Python web development with FastAPI.**
> 
> This project documents my complete learning journey — starting with the fundamentals inspired by **Corey Schafer's FastAPI YouTube course** and expanding into a production-grade backend engineering architecture featuring **asynchronous Python 3.13**, **PostgreSQL**, **SQLAlchemy 2.0 Async**, **Alembic database migrations**, **AWS S3 cloud storage**, **background email tasks**, **automated testing with Pytest & Moto**, and **multi-stage Docker containerization**.

---

## 📑 Table of Contents

- [🎯 Motivation & Learning Goals](#-motivation--learning-goals)
- [🧠 What I Learned: Deep Technical Breakdown](#-what-i-learned-deep-technical-breakdown)
  - [1. FastAPI Core & Modern Python 3.13](#1-fastapi-core--modern-python-313)
  - [2. Asynchronous Python & Event Loop Mastery](#2-asynchronous-python--event-loop-mastery)
  - [3. Database Architecture & SQLAlchemy 2.0 Async](#3-database-architecture--sqlalchemy-20-async)
  - [4. Authentication, Authorization & Security](#4-authentication-authorization--security)
  - [5. Cloud File Uploads & Image Processing (AWS S3 & Pillow)](#5-cloud-file-uploads--image-processing-aws-s3--pillow)
  - [6. Background Tasks & Async Email Workflows](#6-background-tasks--async-email-workflows)
  - [7. Hybrid Full-Stack: Jinja2 SSR + Client JavaScript](#7-hybrid-full-stack-jinja2-ssr--client-javascript)
  - [8. Automated Testing & Cloud Mocking (Pytest & Moto)](#8-automated-testing--cloud-mocking-pytest--moto)
  - [9. Production DevOps & Containerization (UV & Docker)](#9-production-devops--containerization-uv--docker)
- [🛠️ The Evolutionary Journey: How I Built This Project](#️-the-evolutionary-journey-how-i-built-this-project)
- [🔭 Architecture & Application Flow](#-architecture--application-flow)
- [📁 Project Directory Structure](#-project-directory-structure)
- [📡 REST API Reference](#-rest-api-reference)
- [⚙️ Environment Configuration](#️-environment-configuration)
- [🚀 How to Run the Project Locally](#-how-to-run-the-project-locally)
- [🗄️ Database Migrations (Alembic)](#️-database-migrations-alembic)
- [🧪 Database Seeding & S3 Diagnostics](#-database-seeding--s3-diagnostics)
- [🚦 Running the Automated Tests](#-running-the-automated-tests)
- [🐳 Running with Docker](#-running-with-docker)
- [💭 Key Takeaways & Reflections](#-key-takeaways--reflections)
- [👏 Credits & Acknowledgments](#-credits--acknowledgments)

---

## 🎯 Motivation & Learning Goals

When learning web development with Python, it is easy to stop at a basic "Hello World" or simple CRUD app with an in-memory list. My goal for this project was fundamentally different:

1. **Build Everything from Scratch**: Gain a deep, intuitive understanding of how every single component works — from HTTP request parsing to database connection pooling and cloud uploads.
2. **Embrace 100% Asynchronous I/O**: Learn how to write truly non-blocking asynchronous Python using `async`/`await`, ensuring high throughput and concurrency.
3. **Graduate to Production Standards**: Move beyond SQLite into **PostgreSQL** with **Alembic migrations**, secure password hashing (**Argon2**), cloud object storage (**AWS S3**), isolated **Pytest** suites, and **Docker** deployment.
4. **Understand Real-World Trade-Offs**: Learn why certain libraries are chosen (e.g., `uv` vs `pip`, `asyncpg` vs synchronous drivers, `pwdlib` vs legacy `passlib`, `run_in_threadpool` for CPU/blocking tasks).

---

## 🧠 What I Learned: Deep Technical Breakdown

### 1. FastAPI Core & Modern Python 3.13
- **Dependency Injection System (`Depends`)**:
  - Learned how FastAPI's dependency injection container works for database session lifecycle management (`get_db`) and authentication guards (`CurrentUser`).
  - Understood how dependencies can yield a resource (like an `AsyncSession`), automatically ensuring cleanup and rollback after the route handler completes.
- **Modern Python 3.13 Type Hints**:
  - Replaced legacy `typing.Optional` and `typing.Union` with modern union syntax (`str | None`).
  - Leveraged `typing.Annotated` for clean metadata-driven endpoint signatures, separating data types from validation queries and dependency injection declarations.
- **Pydantic v2 Schema Modeling**:
  - Implemented strict separation between **internal database models** and **external API contracts** (`UserCreate`, `UserPublic`, `UserPrivate`, `PostCreate`, `PostResponse`, `PaginatedPostsResponse`).
  - Used `model_config = ConfigDict(from_attributes=True)` to enable automatic ORM-to-schema serialization.
  - Enforced string constraints, email format verification (`EmailStr`), and input sanitization directly at the boundary.
- **Application Lifespan Events (`lifespan`)**:
  - Implemented the modern `@asynccontextmanager` pattern for FastAPI startup and shutdown routines, deprecating legacy `@app.on_event("startup")` hooks.
- **Modular Route Organization with `APIRouter`**:
  - Deconstructed a monolithic `main.py` into dedicated, self-contained routers ([`routers/users.py`](file:///routers/users.py) and [`routers/posts.py`](file:///routers/posts.py)) with individual tags, prefixes, and response models.

---

### 2. Asynchronous Python & Event Loop Mastery
- **The Asyncio Event Loop**:
  - Understood that asynchronous Python runs on a single-threaded cooperative event loop. Any blocking call (such as synchronous file I/O, CPU-heavy image compression, or synchronous network requests) freezes the entire server for all connected clients.
- **Bridging Blocking Calls with `run_in_threadpool`**:
  - Learned how to safely run synchronous or CPU-intensive libraries (such as Pillow image cropping and Boto3 AWS uploads) without stalling the event loop using Starlette's `run_in_threadpool`:
    ```python
    processed_bytes, new_filename = await run_in_threadpool(process_profile_image, content)
    await run_in_threadpool(_upload_to_s3, file_bytes, key)
    ```
- **Asynchronous Drivers**:
  - Adopted `asyncpg` for PostgreSQL and `aiosmtplib` for email delivery to ensure that all database queries and SMTP communications yield execution back to the event loop.
- **Platform-Specific Event Loop Policies**:
  - Solved Windows-specific event loop issues when running async tasks and tests by configuring `WindowsSelectorEventLoopPolicy`.

---

### 3. Database Architecture & SQLAlchemy 2.0 Async
- **SQLAlchemy 2.0 Modern Declarative Mapping**:
  - Implemented type-safe models using `Mapped[...]` and `mapped_column(...)`, replacing older SQLAlchemy 1.x patterns.
- **Relational Integrity & Cascades**:
  - Configured foreign keys (`ForeignKey("users.id")`) and two-way relationships (`relationship(...)`).
  - Implemented `cascade="all, delete-orphan"` to guarantee that deleting a user cleanly purges all associated posts and active password reset tokens without leaving orphan records.
- **Conquering the N+1 Query Problem**:
  - Learned how naive ORM relationship access can execute an additional SQL query for every single post author in a feed (N+1 queries).
  - Solved this using eager loading with `selectinload(models.Post.author)`:
    ```python
    result = await db.execute(
        select(models.Post)
        .options(selectinload(models.Post.author))
        .order_by(models.Post.date_posted.desc())
        .limit(limit)
    )
    ```
- **Database Migrations with Alembic**:
  - Learned how to manage schema evolution safely over time without destroying existing production data.
  - Configured [`alembic/env.py`](file:///alembic/env.py) to run asynchronous migrations using `async_engine_from_config` and `connection.run_sync`.
  - Authored and applied migrations for the initial schema and subsequent column additions (e.g., adding `likes` to `posts`).

---

### 4. Authentication, Authorization & Security
- **Modern Password Hashing with Argon2**:
  - Avoided deprecated libraries (`passlib`) and implemented `pwdlib[argon2]`, the winner of the Password Hashing Competition, ensuring robust protection against brute-force attacks.
- **JSON Web Tokens (JWT) & Stateless Auth**:
  - Implemented the OAuth2 Password Bearer specification (`OAuth2PasswordRequestForm`).
  - Created signed JWT tokens using `pyjwt` with expiration timestamps (`exp`) and subject claims (`sub`).
  - Built an authentication dependency (`get_current_user`) that parses bearer tokens, verifies signatures, checks expiration, and retrieves the active user from the database.
- **Object-Level Authorization & Route Guards**:
  - Learned that authenticating *who* a user is does not automatically authorize *what* they can do.
  - Implemented ownership verification checks preventing users from editing or deleting posts authored by someone else (`HTTP 403 Forbidden`).
- **Cryptographically Secure Password Resets**:
  - Generated unpredictable 32-byte URL-safe reset tokens (`secrets.token_urlsafe(32)`).
  - Stored only the SHA-256 hash (`hashlib.sha256`) of the reset token in the database, ensuring that even a database dump cannot expose usable reset links.
  - Bound reset tokens to a strict 1-hour expiration window with single-use invalidation upon password reset.
- **Defense in Depth & HTTP Security Headers**:
  - Created custom middleware in [`main.py`](file:///main.py) injecting essential HTTP security headers on all responses:
    - `X-Frame-Options: SAMEORIGIN` (prevents clickjacking attacks).
    - `X-Content-Type-Options: nosniff` (prevents MIME-type sniffing).
    - `Referrer-Policy: strict-origin-when-cross-origin`.
    - `Strict-Transport-Security` (HSTS) on production hostnames.
    - `Referrer-Policy: no-referrer` on the password reset page to protect secret query tokens from third-party leakage.
- **Dual-Mode Content Negotiation for Error Handling**:
  - Built unified exception handlers for `StarletteHTTPException` and `RequestValidationError`.
  - Automatically routes errors based on request path: REST API clients receive clean RFC-compliant JSON (`{"detail": "..."}`), while web browsers receive a styled HTML error page (`error.html`).

---

### 5. Cloud File Uploads & Image Processing (AWS S3 & Pillow)
- **File Upload Validation**:
  - Implemented multipart form handling with `UploadFile`.
  - Enforced a hard 5MB file size limit to prevent denial-of-service (DoS) storage exhaustion.
  - Handled invalid file payloads gracefully by catching `PIL.UnidentifiedImageError`.
- **Automated Image Optimization with Pillow**:
  - Corrected image orientation based on digital camera metadata using `ImageOps.exif_transpose`.
  - Automatically cropped non-square pictures into perfectly centered 300x300 thumbnails using `ImageOps.fit` with **LANCZOS** resampling.
  - Sanitized color modes: converted transparency channels (`RGBA`, `LA`, `P`) into clean standard RGB JPEG format at 85% quality.
- **AWS S3 Cloud Integration via Boto3**:
  - Transitioned from ephemeral local filesystem storage to scalable cloud storage on Amazon Web Services S3.
  - Structured bucket keys with organized namespaces (`profile_pics/<uuid>.jpg`).
  - Implemented automatic deletion of old avatar files in S3 when a user uploads a new picture or deletes their account, preventing cloud storage bloat.
  - Authored least-privilege AWS IAM policies ([`aws_iam_policy.json`](file:///aws_iam_policy.json)) and bucket access policies ([`aws_bucket_policy.json`](file:///aws_bucket_policy.json)).

---

### 6. Background Tasks & Async Email Workflows
- **Non-Blocking Background Tasks (`BackgroundTasks`)**:
  - Understood that sending emails involves synchronous network handshakes with an SMTP server (2-5 seconds). Holding an HTTP connection open during this process degrades user experience and exhausts server workers.
  - Offloaded email delivery to FastAPI's built-in `BackgroundTasks`, returning an instant `202 Accepted` response to the client.
- **Async SMTP with `aiosmtplib`**:
  - Integrated `aiosmtplib` with STARTTLS encryption to communicate with SMTP relays (e.g., Mailtrap, Amazon SES, SendGrid).
- **Branded Email Templating**:
  - Created dual-format emails: rich responsive HTML emails rendered via Jinja2 templates ([`templates/email/password_reset.html`](file:///templates/email/password_reset.html)) alongside a clean plain-text fallback.
- **Anti-Enumeration Protection**:
  - Ensured the forgot-password endpoint returns an identical generic confirmation message regardless of whether the submitted email address is registered, preventing attackers from harvesting valid user accounts.

---

### 7. Hybrid Full-Stack: Jinja2 SSR + Client JavaScript
- **Server-Side Rendering (SSR)**:
  - Utilized Jinja2 template inheritance (`layout.html` base template with blocks for content and scripts) for instant initial page rendering and optimal SEO.
- **Client-Side Asynchronous JavaScript**:
  - Built custom vanilla JavaScript modules ([`static/js/auth.js`](file:///static/js/auth.js) and [`static/js/utils.js`](file:///static/js/utils.js)) to communicate with the REST API using `fetch()`.
  - Implemented client-side JWT token storage in `localStorage` with automated inclusion of `Authorization: Bearer <token>` headers on authenticated API requests.
- **Dynamic "Load More" Pagination**:
  - Implemented seamless client-side pagination: when the user clicks "Load More", JavaScript requests the next slice of posts (`?skip=...&limit=...`) and dynamically constructs and injects HTML post cards into the DOM without a page refresh.

---

### 8. Automated Testing & Cloud Mocking (Pytest & Moto)
- **Async Test Harness**:
  - Configured `pytest` with `pytest-anyio` to test asynchronous FastAPI endpoints using `httpx.AsyncClient` with `ASGITransport`.
- **Database Session Isolation via Savepoints**:
  - Learned how to run database tests safely without polluting the test database:
  - Configured a `db_session` fixture that wraps each test inside an isolated transaction savepoint (`create_savepoint`) and rolls back immediately after test completion.
- **Mocking Cloud Infrastructure with Moto**:
  - Used `moto[s3]` to spin up an in-memory mock AWS S3 service during testing.
  - Verified that avatar upload endpoints correctly transfer files to S3 and verify bucket contents without touching live AWS infrastructure or incurring cloud costs.
- **Mocking External Services**:
  - Used `unittest.mock.AsyncMock` to verify that password reset emails are dispatched with correct recipient addresses and valid tokens without needing a live mail server.

---

### 9. Production DevOps & Containerization (UV & Docker)
- **Astral `uv` Package Management**:
  - Used `uv` to manage Python versions (`.python-version`), generate deterministic lockfiles (`uv.lock`), and execute scripts with sub-second dependency installation.
- **Multi-Stage Docker Architecture**:
  - Built a production-ready, multi-stage [`Dockerfile`](file:///Dockerfile):
    - **Builder Stage**: Uses official `ghcr.io/astral-sh/uv` binary to install locked dependencies with bytecode compilation (`UV_COMPILE_BYTECODE=1`).
    - **Final Stage**: Creates a clean `python:3.13-slim` image containing only the virtual environment and application code.
- **Container Security & Process Management**:
  - Created a dedicated non-root user (`appuser`) to run the application securely.
  - Used `exec fastapi run` to ensure Uvicorn receives process termination signals (SIGTERM) directly from the Docker daemon for clean connection draining and graceful shutdowns.

---

## 🛠️ The Evolutionary Journey: How I Built This Project

```mermaid
timeline
    title Project Development & Learning Milestones
    Phase 1 to 3 : Initial Setup & In-Memory REST API
                 : Jinja2 Server-Side Templates
                 : Pydantic Validation & Custom Error Handling
    Phase 4 to 6 : SQLAlchemy ORM & Relational Models
                 : Full Asynchronous Refactor (async/await)
                 : Route Modularization with APIRouter
    Phase 7 to 9 : Dynamic Frontend JavaScript Integration
                 : JWT Authentication & Argon2 Password Hashing
                 : Pillow Image Optimization Pipeline
    Phase 10 to 12 : Scalable Offset/Limit Pagination
                   : Asynchronous Email & Password Resets
                   : PostgreSQL Migration & Alembic
    Phase 13 to 15 : AWS S3 Cloud Storage Integration
                   : Pytest & Moto Automated Test Suite
                   : Production Docker Containerization
```

| Phase | Milestone | What Was Built & Key Learning |
|:---:|:---|:---|
| **1** | **Foundations & REST API Prototype** | Initialized the project with Python 3.13 and `uv`. Started with in-memory dictionaries ([`snippets.txt`](file:///snippets.txt)) to master HTTP methods (`GET`, `POST`), route parameters, and status codes. |
| **2** | **Jinja2 Frontend Integration** | Mounted static asset directories (`/static`, `/media`) and introduced Jinja2 templates (`layout.html`, `home.html`, `post.html`) to deliver styled views using Bootstrap. |
| **3** | **Pydantic Validation & Error Handling** | Designed Pydantic v2 schemas (`UserCreate`, `UserPublic`, `PostCreate`, `PostResponse`). Built dual-mode exception handling (JSON for `/api/*`, styled HTML for browser navigation). |
| **4** | **SQLAlchemy Models & Relational DB** | Replaced in-memory lists with a relational database. Defined `User` and `Post` declarative models, foreign keys, cascades (`all, delete-orphan`), and relationship back-references. |
| **5** | **Full Asynchronous Refactoring** | Migrated the entire database layer from synchronous SQLAlchemy to SQLAlchemy 2.0 `create_async_engine` and `AsyncSession`, refactoring all queries to async `select()`. |
| **6** | **Modularization with APIRouter** | Refactored the monolithic application into distinct, modular routers ([`routers/users.py`](file:///routers/users.py) and [`routers/posts.py`](file:///routers/posts.py)) with clean tags and URL prefixes. |
| **7** | **Interactive Client JavaScript** | Created [`auth.js`](file:///static/js/auth.js) and [`utils.js`](file:///static/js/utils.js) to bridge the frontend with the API. Implemented token persistence, dynamic login/logout UI states, and modal post creation. |
| **8** | **JWT Authentication & Ownership Authorization** | Implemented OAuth2 password flow, `pwdlib` with Argon2 password hashing, JWT generation, and `CurrentUser` dependency injection to enforce ownership checks. |
| **9** | **Pillow Image Processing Pipeline** | Built avatar uploading with image sanitization, square cropping (`ImageOps.fit`), EXIF auto-rotation, and JPEG optimization. |
| **10** | **Scalable Offset/Limit Pagination** | Implemented query-based pagination (`skip`, `limit`) with total counts and built a dynamic "Load More" frontend button. |
| **11** | **Async Email & Password Reset Flow** | Designed `PasswordResetToken` table, crypto-secure URL tokens, SHA-256 token hashing, `aiosmtplib` integration, and FastAPI `BackgroundTasks`. |
| **12** | **PostgreSQL & Alembic Migrations** | Transitioned the database layer to PostgreSQL with `asyncpg`. Integrated Alembic with async migration support (`run_async_migrations`) and generated initial migration scripts. |
| **13** | **Cloud Storage with AWS S3 & Boto3** | Replaced local disk storage with Amazon S3. Configured Boto3 client, IAM policies, public read bucket policies, and background thread execution via `run_in_threadpool`. |
| **14** | **Comprehensive Testing Suite** | Built a robust test harness using `pytest`, `pytest-anyio`, and `moto[s3]`. Implemented transaction-rollback database fixtures and mocked AWS S3 and email services. |
| **15** | **Containerization with Docker** | Created a production-ready, multi-stage `Dockerfile` using `python:3.13-slim` and `uv`, running with a non-root user (`appuser`) and graceful SIGTERM handling. |

---

## 🔭 Architecture & Application Flow

```mermaid
flowchart TD
    Client["Client / Web Browser"]
    
    subgraph FastAPI_Application["FastAPI Application"]
        Middleware["Security Headers Middleware\n(HSTS, X-Frame-Options, CSP, nosniff)"]
        ExceptionRouter{"Request Type"}
        API_Handler["API JSON Exception Handler"]
        HTML_Handler["Jinja2 Error Template Handler"]
        
        APIRouter["API Routers\n(/api/users & /api/posts)"]
        JinjaViews["Server-Side Rendered Views\n(Jinja2 Templates)"]
        
        Auth["Auth & Security Engine\n(JWT + Argon2 via pwdlib)"]
        BGTasks["Background Tasks Engine\n(Email Dispatcher)"]
        ImgProc["Image Processor\n(Pillow in Threadpool)"]
    end
    
    subgraph External_Services["Datastores & External Services"]
        PG[(PostgreSQL Database\nAsync via asyncpg)]
        S3["AWS S3 Cloud Storage\n(Profile Avatars via Boto3)"]
        SMTP["SMTP Mail Server\n(Async aiosmtplib)"]
    end

    Client -->|HTTP / HTTPS| Middleware
    Middleware --> ExceptionRouter
    ExceptionRouter -->|/api/*| API_Handler
    ExceptionRouter -->|Browser Pages| HTML_Handler
    
    Middleware --> APIRouter
    Middleware --> JinjaViews
    
    APIRouter --> Auth
    APIRouter --> ImgProc
    APIRouter --> BGTasks
    
    Auth --> PG
    APIRouter --> PG
    JinjaViews --> PG
    
    ImgProc -->|Upload / Delete| S3
    BGTasks -->|Send Reset Emails| SMTP
```

---

## 📁 Project Directory Structure

```text
FastApi Blog App/
├── .dockerignore                       # Excludes git, tests, and caches from Docker builds
├── .env.example                        # Documented environment variable template
├── .gitignore                          # Comprehensive ignores for Python, DBs, caches, OS
├── .python-version                     # Python version pin (3.13)
├── Dockerfile                          # Multi-stage production container definition
├── README.md                           # Project documentation & learning journal
├── pyproject.toml                      # Project metadata, dependencies, and dev tools (uv)
├── uv.lock                             # Cryptographically locked dependency graph
│
├── alembic.ini                         # Alembic database migration configuration
├── alembic/                            # Migration environment and version scripts
│   ├── env.py                          # Asynchronous migration runner
│   └── versions/                       # Versioned migration revision files
│
├── auth.py                             # JWT token creation, verification, and CurrentUser dependency
├── config.py                           # Pydantic BaseSettings loading .env configuration
├── database.py                         # Async SQLAlchemy engine, session maker, and get_db dependency
├── models.py                           # SQLAlchemy ORM models (User, Post, PasswordResetToken)
├── schemas.py                          # Pydantic request/response validation schemas
├── email_utils.py                      # Async email sender using aiosmtplib and Jinja2 templates
├── image_utils.py                      # Pillow image optimization & Boto3 AWS S3 upload/delete helpers
├── main.py                             # FastAPI app instance, middleware, SSR routes, exception handlers
│
├── routers/                            # Modular API endpoints
│   ├── __init__.py
│   ├── posts.py                        # /api/posts routes (CRUD, pagination, authorization)
│   └── users.py                        # /api/users routes (Auth, profile, S3 avatars, password reset)
│
├── static/                             # Static public assets
│   ├── css/                            # Bootstrap and custom stylesheets
│   ├── js/                             # Client-side JavaScript (auth.js, utils.js)
│   ├── icons/                          # Favicons and webmanifest assets
│   └── profile_pics/                   # Default avatar fallback (default.jpg)
│
├── templates/                          # Jinja2 HTML templates
│   ├── account.html                    # User profile, password change, and avatar upload page
│   ├── error.html                      # Branded error page for browser navigation
│   ├── forgot_password.html            # Password reset request form
│   ├── home.html                       # Blog home feed with dynamic "Load More"
│   ├── layout.html                     # Base HTML shell with navigation and modals
│   ├── login.html                      # User login interface
│   ├── post.html                       # Individual post view and edit/delete modal
│   ├── register.html                   # Account registration form
│   ├── reset_password.html             # Set new password form (Referrer-Policy: no-referrer)
│   ├── user_posts.html                 # Filtered posts by a specific author
│   └── email/                          # Email templates
│       └── password_reset.html         # Styled HTML password reset email
│
├── tests/                              # Automated test suite
│   ├── conftest.py                     # Pytest fixtures (async client, DB rollback, moto S3)
│   ├── test_posts.py                   # Tests for post creation, retrieval, updates, permissions
│   └── test_users.py                   # Tests for registration, auth, S3 upload, password reset
│
├── aws_bucket_policy.json              # Sample AWS S3 public read policy for profile_pics/*
├── aws_iam_policy.json                 # Sample AWS IAM policy granting PutObject/DeleteObject
├── check_s3.py                         # Standalone diagnostic utility to verify S3 credentials
└── populate_db.py                      # Database seeder populating users, posts, and S3 avatars
```

---

## 📡 REST API Reference

Interactive API documentation is automatically generated by FastAPI:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Authentication & User Endpoints (`/api/users`)

| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---:|
| `POST` | `/api/users` | Register a new user account | No |
| `POST` | `/api/users/token` | Obtain JWT access token (OAuth2 Form: `username`, `password`) | No |
| `GET` | `/api/users/me` | Fetch currently authenticated user's profile | **Yes (Bearer)** |
| `GET` | `/api/users/{user_id}` | Fetch public profile by user ID | No |
| `PATCH` | `/api/users/{user_id}` | Update username or email | **Yes (Owner)** |
| `DELETE`| `/api/users/{user_id}` | Delete user account and cleanup avatar | **Yes (Owner)** |
| `PATCH` | `/api/users/{user_id}/picture` | Upload and process profile picture to AWS S3 | **Yes (Owner)** |
| `DELETE`| `/api/users/{user_id}/picture` | Delete profile picture from AWS S3 | **Yes (Owner)** |
| `PATCH` | `/api/users/me/password` | Change password for authenticated user | **Yes (Bearer)** |
| `POST` | `/api/users/forgot-password` | Request password reset email via background task | No |
| `POST` | `/api/users/reset-password` | Reset password using one-time token | No |
| `GET` | `/api/users/{user_id}/posts` | Fetch paginated posts authored by specific user | No |

### Blog Post Endpoints (`/api/posts`)

| Method | Endpoint | Description | Auth Required |
|:---|:---|:---|:---:|
| `GET` | `/api/posts` | Get paginated list of posts (`?skip=0&limit=10`) | No |
| `POST` | `/api/posts` | Create a new blog post | **Yes (Bearer)** |
| `GET` | `/api/posts/{post_id}` | Retrieve a single post by ID | No |
| `PUT` | `/api/posts/{post_id}` | Full update of a post | **Yes (Author)** |
| `PATCH` | `/api/posts/{post_id}` | Partial update of post title or content | **Yes (Author)** |
| `DELETE`| `/api/posts/{post_id}` | Delete a post | **Yes (Author)** |

### Health Check Endpoint

| Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/health` | Verifies database connectivity (`SELECT 1`) for container health monitoring |

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root based on [`.env.example`](file:///.env.example):

```bash
cp .env.example .env
```

| Variable | Type | Default | Description |
|:---|:---:|:---:|:---|
| `DATABASE_URL` | string | *Required* | Async SQLAlchemy connection string (e.g., `postgresql+asyncpg://user:pass@localhost:5432/blog`) |
| `SECRET_KEY` | string | *Required* | High-entropy secret key for JWT signing (`openssl rand -hex 32`) |
| `ALGORITHM` | string | `HS256` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | int | `30` | JWT expiration duration in minutes |
| `RESET_TOKEN_EXPIRE_MINUTES` | int | `60` | Password reset token validity window |
| `S3_BUCKET_NAME` | string | *Required* | AWS S3 bucket name for profile picture uploads |
| `S3_REGION` | string | `us-east-1` | AWS S3 region |
| `S3_ACCESS_KEY_ID` | string | `None` | AWS IAM access key ID |
| `S3_SECRET_ACCESS_KEY` | string | `None` | AWS IAM secret access key |
| `S3_ENDPOINT_URL` | string | `None` | Custom S3 endpoint (optional, for MinIO or LocalStack) |
| `MAX_UPLOAD_SIZE_BYTES` | int | `5242880` | Maximum file upload size (default: 5 MB) |
| `POSTS_PER_PAGE` | int | `10` | Default number of posts returned per page |
| `MAIL_SERVER` | string | `localhost` | SMTP server host (e.g., `sandbox.smtp.mailtrap.io`) |
| `MAIL_PORT` | int | `587` | SMTP port (`587` for TLS, `2525` for Mailtrap) |
| `MAIL_USERNAME` | string | `""` | SMTP authentication username |
| `MAIL_PASSWORD` | string | `""` | SMTP authentication password |
| `MAIL_FROM` | string | `noreply@example.com` | Sender email address |
| `MAIL_USE_TLS` | bool | `True` | Enable STARTTLS encryption for email dispatch |
| `FRONTEND_URL` | string | `http://localhost:8000` | Base URL used to construct password reset links |

---

## 🚀 How to Run the Project Locally

### 1. Prerequisites
- **Python 3.13+** installed
- **[uv](https://docs.astral.sh/uv/)** installed (recommended) or `pip`
- **PostgreSQL** running locally or via Docker

### 2. Clone the Repository & Install Dependencies
```bash
git clone https://github.com/raihan12121/Fastapi-Web-App-from-scratch-for-Practice.git
cd "FastApi Blog App"

# Install all dependencies with uv
uv sync
```

*(Alternatively with standard virtual environment and pip)*:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### 3. Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env with your PostgreSQL credentials, SECRET_KEY, and AWS S3 bucket settings
```

### 4. Apply Database Migrations
```bash
uv run alembic upgrade head
```

### 5. Start the Development Server
```bash
uv run fastapi dev main.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🗄️ Database Migrations (Alembic)

The project uses **Alembic** configured for asynchronous SQLAlchemy.

- **Apply all migrations**:
  ```bash
  uv run alembic upgrade head
  ```
- **Generate a new migration after editing models**:
  ```bash
  uv run alembic revision --autogenerate -m "describe_your_changes"
  ```
- **Revert the last migration**:
  ```bash
  uv run alembic downgrade -1
  ```
- **Inspect migration history**:
  ```bash
  uv run alembic history --verbose
  ```

---

## 🧪 Database Seeding & S3 Diagnostics

### 1. S3 Connectivity Test
Quickly test your AWS S3 bucket permissions without running the full app:
```bash
uv run python check_s3.py
```
This script uploads a test file to `profile_pics/` and deletes it, verifying that your AWS credentials and policies are correctly configured.

### 2. Seed Sample Data
Populate the database with test users, sample posts across multiple dates, and uploaded sample avatars:
```bash
uv run python populate_db.py
```

---

## 🚦 Running the Automated Tests

The test suite runs with **Pytest**, **AnyIO**, and **Moto**.

```bash
# Run all tests
uv run pytest

# Run with verbose output and duration timing
uv run pytest -v --durations=5
```

All 12 test cases test isolated database transactions with automated rollback, S3 uploads via in-memory Moto mocks, and asynchronous email triggers without external side-effects.

---

## 🐳 Running with Docker

The application includes a multi-stage, non-root Docker build.

### 1. Build the Docker Image
```bash
docker build -t fastapi-blog-app:latest .
```

### 2. Run the Container
```bash
docker run -d \
  --name fastapi-blog \
  -p 8080:8080 \
  --env-file .env \
  fastapi-blog-app:latest
```
Access the application at [http://localhost:8080](http://localhost:8080).

---

## 💭 Key Takeaways & Reflections

Building this application from scratch was an invaluable learning experience:
- **Async Isn't Just Syntax**: Learning when to use `async/await` versus when a task must be handed off to a threadpool (`run_in_threadpool`) was a major architectural breakthrough.
- **Security is Multi-Layered**: True security requires defense-in-depth: Argon2 hashing, stateless JWT tokens, object-level authorization guards, cryptographic token hashing for password resets, and HTTP security headers.
- **Testing Saves Time**: Setting up `moto` for S3 mocking and database rollback fixtures using savepoints allowed rapid, confident refactoring without breaking features.
- **Tooling Matters**: Switching to Astral's `uv` dramatically improved dependency management speed, and multi-stage Docker builds made production packaging clean and lightweight.

---

## 👏 Credits & Acknowledgments

- **Core Foundation**: Deep gratitude to **Corey Schafer** for his outstanding FastAPI YouTube series, which provided the foundational tutorial and inspiration for this project.
- **Author**: Built with dedication by **Muhammad Raihan** as a deep-dive learning and practice project.

---

## 📄 License

This project is licensed under the MIT License — feel free to use it for learning, practice, and reference!
