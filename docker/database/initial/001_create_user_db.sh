psql << EOF
    CREATE USER "django-shop" WITH PASSWORD 'django-shop';
    ALTER ROLE "django-shop" SUPERUSER;
    CREATE DATABASE "django-shop";
    GRANT ALL PRIVILEGES ON DATABASE "django-shop" to "django-shop";
EOF
