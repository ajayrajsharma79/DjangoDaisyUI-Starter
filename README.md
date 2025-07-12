# DjangoDaisyUI Starter Project

A Django starter project designed for rapid development, featuring TailwindCSS with DaisyUI and PostgreSQL integration. Use this as a base for your own Django projects.

## Features
- Django 5.2.4
- TailwindCSS 4.1.11
- DaisyUI 5.0.46 for modern UI
- PostgreSQL 17 database support
- Custom user model
- Ready-to-use static and template structure

## Getting Started

### 1. Fork or Clone the Repository

- **Fork:** Click the "Fork" button on GitHub to create your own copy.
- **Clone:**
  ```sh
  git clone https://github.com/<your-username>/DjangoDaisyUI-Starter.git
  cd DjangoDaisyUI-Starter
  ```

### 2. Set Up Python Environment

- Create a virtual environment:
  ```sh
  python -m venv .venv
  ```
- Activate it:
  - **Windows (PowerShell):**
    ```sh
    .venv\Scripts\Activate.ps1
    ```
  - **macOS/Linux:**
    ```sh
    source .venv/bin/activate
    ```
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### 3. Set Up Node.js for TailwindCSS/DaisyUI

- Install Node.js (if not already installed)
- Install dependencies:
  ```sh
  npm install
  ```
- Build TailwindCSS:
  ```sh
  npm run build:css
  ```


### 4. Configure Environment Variables

- Copy `.env.example` to `.env` and fill in your values:
  ```sh
  cp .env.example .env
  ```
- Set your `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and database settings.

### 5. Set Up PostgreSQL

- Ensure PostgreSQL is running and accessible.
- Edit `.pg_service.conf` with your database credentials.
- Optionally, set the `PGSERVICEFILE` environment variable:
  ```sh
  $env:PGSERVICEFILE="C:\path\to\.pg_service.conf"  # Windows
  export PGSERVICEFILE=/path/to/.pg_service.conf        # macOS/Linux
  ```

### 6. Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 7. Start Development Server

- Monitory CSS chages during live development:
  ```sh
  npm run watch:css
  ```

- Start Django Server
```sh
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Customization
- Add your own Django apps in the `core/` or `users/` directories.
- Customize templates in `templates/` and static files in `static/`.
- Modify TailwindCSS/DaisyUI config in `tailwind.config.js`.

## License
MIT

---

Feel free to use this starter for your own Django projects. Contributions welcome!
