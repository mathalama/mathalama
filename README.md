<a href="https://github.com/mathalama">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg">
    <source media="(prefers-color-scheme: light)" srcset="light_mode.svg">
    <img alt="Aikyn Sagyntai — GitHub profile" src="light_mode.svg" width="100%">
  </picture>
</a>

## About

I'm **Aikyn Sagyntai**, a backend developer and DevOps engineer from **Astana, Kazakhstan**. I work with **Java**, **Go** and **Python**, and study Software Engineering at **Astana IT University** (2024 – 2027).

I like building systems end to end: designing the database, splitting services, wiring queues and caches, packaging everything in Docker and shipping it through CI/CD. I'm interested in distributed systems and backend architecture for products at real production scale.

**Currently**

- DevOps Engineer at **WONK**
- Building **Zovik**, a self-hosted CI/CD server with Docker-based build isolation and DAG pipeline visualization
- Building an **Identity & Verification Platform**, a distributed auth and onboarding system with AI document verification
- Building **Qolda**, a donation-alert platform for streamers
- Backend lead of my diploma project **MedExchange**, secure medical document exchange between clinics

Portfolio: [mathalama.dev](https://www.mathalama.dev)

---

## Tech stack

| Area | Technologies |
|:--|:--|
| **Languages** | Java, Go, Python, TypeScript, JavaScript, Rust, Dart, SQL |
| **Backend** | Spring Boot 4, Spring Security, OAuth2 Authorization Server, Spring Data JPA, Gin, Chi, FastAPI, gRPC, REST, WebSockets (STOMP), WebRTC |
| **Data** | PostgreSQL, Redis, MySQL, H2, Flyway, Alembic, golang-migrate, SQLAlchemy 2.0 (async), pgx |
| **Messaging** | Apache Kafka, NATS |
| **Frontend** | React, Next.js, Vue 3, Vite, Tailwind CSS, React Query, Zustand |
| **Desktop and mobile** | Tauri 2 (Rust), Flutter |
| **DevOps** | Docker, Docker Compose, Kubernetes, Helm, Terraform, Ansible, Caddy, Nginx, Let's Encrypt, GitHub Actions (incl. self-hosted runners), GitLab CI, GHCR |
| **Security** | gitleaks, pre-commit hooks, actionlint |
| **Observability** | Prometheus, Grafana, Loki, Zipkin |
| **Storage** | S3, MinIO |
| **Testing** | JUnit 5, Mockito, JaCoCo, Playwright, Vitest |
| **AI and ML** | YOLOv8, faster-whisper, EasyOCR, DeepFace, OpenCV, Google Gemini API |
| **Tools** | IntelliJ IDEA, VS Code, Git, Postman, Linux (Ubuntu) |

---

## Experience

**DevOps Engineer — WONK**
*September 2026 – present · Astana*
- Moved dev deployments of 13 repositories from GitHub-hosted runners to a self-hosted runner inside the company network, reducing the dev server's external attack surface; audited the workflows and prepared a staged rollout plan
- Made deploy jobs safe for a persistent shared runner: temporary SSH credentials live only in the job's temporary directory and never in the runner's home directory
- Added a pre-deploy check to GitHub Actions workflows that blocks deploying a branch that is behind `dev`, plus job timeouts; verified the logic locally on full and shallow clones
- Introduced secret scanning with gitleaks and pre-commit hooks, scanned repository history and tuned the configuration to keep false positives low without disabling detection rules
- Fixed inaccurate metrics in a multi-process Python (FastAPI / uvicorn) service, where each worker reported only its own counters; compared aggregation approaches and covered the fix with a regression test
- Wrote architecture documentation for the dev environment: service map, reverse-proxy routing and TLS certificates, the path from commit to running container, data stores and migrations, and the differences from the Kubernetes-based production setup

**Backend Developer — colo.ai**
*March 2026 – June 2026*
- Designed and built the backend for a medical imaging analysis platform from scratch: FastAPI, async PostgreSQL / SQLAlchemy 2.0, Redis, S3 — 10 domain modules, 9 Alembic migrations
- Implemented JWT authentication, RBAC and clinic-level data scoping for patients and studies at the API layer
- Designed the ML integration pipeline with the claim-check pattern (presigned S3 URLs) for asynchronous image analysis, taking file transfer load off the backend
- Set up CI/CD with GitHub Actions: automated build, push to GHCR, SSH deploy with automatic Alembic migrations
- Closed critical pre-production security gaps: rate limiting on auth endpoints, closed public ports in docker-compose, healthchecks, streaming S3 image delivery instead of loading files into memory

**Backend Developer — Kazakhstan Housing Company**
*December 2025 – February 2026 · Astana*
- Implemented XML-to-JSON response parsing for a Go / Gin proxy service integrating with an external SLA API (SimBase)
- Wrote proxy request handlers: upstream forwarding, status and error extraction, response formatting
- Documented the service with a README and a Swagger / OpenAPI spec

**Technical Support Specialist — Infologia**
*October 2024 – January 2026 · Astana*
- Diagnosed and resolved user issues using internal tools and logs
- Managed support tickets and worked with the development team
- Documented recurring issues to improve the support workflow

---

## Featured projects

### [Zovik](https://github.com/mathalama/zovic) — distributed CI/CD and DAG pipeline engine
A lightweight, self-hosted alternative to GitLab CI and Jenkins.
- **Master-agent architecture**: Spring Boot 4 master on Java 21 virtual threads (under ~280 MB RAM) and a ~15 MB stateless **Go runner** with pull-model long polling, so workers need no inbound ports
- **DAG engine**: steps declare `depends_on`, independent stages run in parallel, topological sort with cycle detection
- Every step runs in an isolated **Docker** container (Docker-out-of-Docker) with artifact extraction
- **AES-256-GCM** encrypted secret vault and live log streaming over **STOMP WebSockets**
- **GitHub webhooks** with HMAC-SHA256 verification and commit status reporting
- Vue dashboard with an interactive DAG visualizer

`Java 21` `Spring Boot 4` `Go` `Vue` `PostgreSQL` `Docker` `WebSockets`

### [Identity & Verification Platform](https://github.com/mathalama/SuperApp) — distributed auth and KYC onboarding
Microservices monorepo for authentication, user onboarding and automated KYC verification.
- **Spring API gateway** with JWT authentication and Redis rate limiting
- **Identity service** (auth, OAuth2, sessions), **user service** (profiles, avatars), **KYC service** and **notification service**
- **Apache Kafka** (KRaft) as the event bus between services
- **Python / FastAPI ML service** for document verification: EasyOCR and MRZ reading, face matching with DeepFace (ArcFace), passive liveness check
- React / Vite KYC web dashboard and a **Flutter** mobile app
- PostgreSQL, Redis, MinIO, Zipkin tracing, Kubernetes manifests, gitleaks secret scanning

`Java` `Spring Boot` `Kafka` `Redis` `Python` `FastAPI` `Flutter` `Kubernetes`

### Qolda — donation alerts for streamers *(private, in development)*
A platform that turns payment notifications into on-stream donation alerts.
- **Desktop client** on Tauri 2 (Rust + React) reads Windows notifications and sends them to the API
- **Go API** with PostgreSQL, Redis, S3-compatible media storage and realtime updates for the web app and OBS widgets
- **Python TTS service** (Piper) that voices donation messages
- **Web app** (React / Vite): dashboard, alert settings and widgets, plus a separate landing site

`Go` `Rust` `Tauri` `React` `TypeScript` `PostgreSQL` `Redis` `S3` `Python`

### [Mathalama Talk](https://github.com/mathalama/mathalama-talk) — anonymous chat and voice calls
Instant anonymous chat: match by interests, talk in private rooms or start a real-time voice call. No registration needed.
- **Go microservices**: API gateway, user, matchmaking, chat (WebRTC signaling), moderation and notification services
- **NATS** for events, **Redis** for sessions and queues, **PostgreSQL**, **coturn** for WebRTC TURN
- **Next.js** frontend and shared Protobuf libraries
- Infrastructure: Docker, Kubernetes, Ansible, Terraform, Prometheus / Grafana / Loki, load tests

`Go` `Next.js` `NATS` `Redis` `PostgreSQL` `WebRTC` `Kubernetes` `Terraform`

### [Identity Service](https://github.com/mathalama/identity-service) — authentication microservice
Production-ready auth service built with clean architecture.
- JWT access and refresh tokens with rotation, **Redis** blacklist on logout
- **OAuth2 Authorization Server** (OIDC, RS256) and **OAuth2 login** with Google and GitHub, with several providers linked to one account
- Roles `USER` / `ADMIN` / `SUPER_ADMIN`, email verification, password reset, resend throttling
- Service-to-service token validation, Flyway migrations, Swagger / OpenAPI

`Java 21` `Spring Boot 4` `Spring Security` `PostgreSQL` `Redis` `Flyway` `Docker`

### [Payment Platform](https://github.com/mathalama/payment-platform) — distributed payments
Microservice platform for money transfers between accounts.
- **API gateway**, **identity**, **account** (balances and an immutable ledger) and **transfer** (idempotent transfer orchestration) services
- Infrastructure as code with **Terraform** and **Ansible**, monitoring with **Prometheus** and **Grafana**
- Separate staging and production Docker Compose setups

`Java` `Spring Boot` `PostgreSQL` `Docker` `Terraform` `Ansible` `Prometheus`

### [Colo.ai API](https://github.com/mathalama/api.colo.ai) — medical AI backend
Backend for a clinical platform that analyzes endoscopy images to detect polyps for early colorectal cancer diagnosis.
- FastAPI (Python 3.12), async SQLAlchemy 2.0, Alembic, PostgreSQL, Redis, MinIO
- Clinics, patients, studies, image upload, AI analysis and PDF reports

`Python` `FastAPI` `PostgreSQL` `Redis` `MinIO` `Docker`

### [Nucla](https://github.com/mathalama/founders) — co-founder matching for startups
Connects founders with co-founders, developers and designers: profiles, startup ideas, open roles and applications.
- Go backend on **Chi**, PostgreSQL via **pgx**, JWT in HttpOnly cookies
- Embedded SQL migrations (`go:embed` + golang-migrate), **Web Push** (VAPID) and SMTP email
- React + Vite + React Query frontend, Caddy and Ansible deployment

`Go` `PostgreSQL` `React` `Caddy` `Ansible`

### [AutoCut](https://github.com/mathalama/autocut) — AI subtitles and silence cutting
Local GPU-powered audio and video toolkit.
- Studio subtitle recorder that produces accurate SRT / TXT and copies them to the clipboard
- Real-time live subtitles for **OBS**, Twitch and YouTube
- Transcription of MP4, MKV, MOV, WAV and MP3 files
- Automatic silence removal with frame-accurate **FFmpeg** cuts
- NVIDIA CUDA + faster-whisper, Windows installer

`Python` `CUDA` `faster-whisper` `FFmpeg`

### [Mathalama Focus](https://github.com/mathalama/focus) — focus and reflection app
Calm-first productivity app with a web UI, REST API, Telegram bot and browser extension.

`Go` `Gin` `PostgreSQL` `React` `TypeScript` `Telegram Bot API`

---

## More projects

| Project | What it is | Stack |
|:--|:--|:--|
| [Medical Scheduling Platform](https://github.com/mathalama/go-microservice) | Appointment, doctor and notification services over gRPC; Redis caching and rate limiting, NATS events, worker-pool background jobs, idempotent mock gateway | Go, gRPC, NATS, Redis, PostgreSQL |
| [VacancyBot](https://github.com/mathalama/tgbot) | Telegram bot that monitors job channels and sends only vacancies matching your CV, with Gemini AI analysis | Go, PostgreSQL, Gemini |
| [Til Bridge](https://github.com/mathalama/til-bridge) | Kazakh Cyrillic and Latin transliteration: REST API, web and mobile apps | Spring Boot, React, Flutter |
| [University Platform](https://github.com/mathalama/review-universities) | University reviews and ratings with email verification, roles and rate limiting | Java, Spring, TypeScript, React |
| [Career Navigator API](https://github.com/mathalama/career-navigator-api) / [UI](https://github.com/mathalama/career-navigator-ui) | Career guidance: JWT auth, mentors, job recommendations, skills tracking, admin panel | Spring Boot 4, PostgreSQL, Vue 3, Tailwind |
| [AI Stylist & Virtual Try-On](https://github.com/mathalama/fashion) | AI outfit recommendations and virtual try-on for a fashion marketplace | Python, TypeScript |
| [mathalama.edu](https://github.com/mathalama/mathalama.edu) | Education platform frontend | Next.js 16, React 19, Tailwind 4, Zustand |
| [Contact Form API](https://github.com/mathalama/contact-form-api) | Layered REST API for contact forms with validation and tests | Spring Boot, JPA, MySQL / H2, JUnit |
| [Spring Auth](https://github.com/mathalama/spring-auth) | Authentication with Spring Security | Spring Boot, Spring Security |
| [Short URL](https://github.com/mathalama/short-url) | URL shortener | Spring Boot |
| [E-commerce Backend](https://github.com/mathalama/e-commerce-backend) | Online store backend | Spring Boot |
| [Task Manager CLI](https://github.com/mathalama/task-manager-cli) | Console task manager | Go |
| [To-Do Console App](https://github.com/mathalama/aveelon.tt) | Layered console to-do app with file persistence | Java |
| [CI/CD Practice](https://github.com/mathalama/ci-cd-practice) | Dockerized app with a GitHub Actions pipeline | Python, Docker |

---

## University coursework (Astana IT University)

| Repository | Topic |
|:--|:--|
| [daa-aitu](https://github.com/mathalama/daa-aitu) | Divide and conquer: MergeSort, QuickSort, Median-of-Medians, Closest Pair, with Master Theorem analysis and metrics |
| [daa-aitu-2](https://github.com/mathalama/daa-aitu-2) | Shell Sort vs Heap Sort: complexity analysis, benchmarks and peer code review |
| [daa-aitu-3](https://github.com/mathalama/daa-aitu-3) | Minimum spanning tree: Prim and Kruskal, JUnit checks, Graphviz visualization |
| [daa-aitu-4](https://github.com/mathalama/daa-aitu-4) | Tarjan SCC, condensation DAG, Kahn topological sort, DAG shortest and longest paths |
| [design-patterns](https://github.com/mathalama/design-patterns), [sdp-aitu](https://github.com/mathalama/sdp-aitu), [bankingSystemSDP](https://github.com/mathalama/bankingSystemSDP) | Software design patterns in Java |
| [frontend-aitu](https://github.com/mathalama/frontend-aitu), [midterm](https://github.com/mathalama/frontend-aitu-midterm), [final](https://github.com/mathalama/frontend-aitu-final-ui), [e-learning](https://github.com/mathalama/e-learning) | Web frontend coursework: HTML, CSS, JavaScript |

---

## Education and certifications

**Astana IT University** — Bachelor's degree, Software Engineering *(August 2024 – July 2027)*

Certifications:
- Introduction to Hardware and Operating Systems
- Linux System Programming and Introduction to Buildroot
- AI Basics: Overview of AI
- Search and AI

---

## Contacts

[![Portfolio](https://img.shields.io/badge/mathalama.dev-000000?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.mathalama.dev)
[![Email](https://img.shields.io/badge/aikyn@mathalama.dev-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aikyn@mathalama.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mathalama)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/mathalama)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/mathalama)
