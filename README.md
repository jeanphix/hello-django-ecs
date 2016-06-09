AWS ECS compliant django application
====================================

Configuration
-------------

PostgreSQL database:

```
export DATABASE_URL=postgres://<user>:<password>@<host>/<name>
```

Secret key:

```
export SECRET_KEY=<secret>
```

Allowed host:

```
export DOMAIN_NAME=<domain>
```

Debug mode:

```
export DEBUG=1
```

S3 storage:

```
export AWS_STORAGE_BUCKET_NAME=<bucket name>
export AWS_ACCESS_KEY_ID=<access key>
export AWS_SECRET_ACCESS_KEY=<secret key>
```

CDN:

```
export CDN_DOMAIN_NAME=<domain>
```
